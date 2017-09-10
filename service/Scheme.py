from random import choice as rchoice


class Scheme:
    peer_review_scheme = [[]]
    all_videos = []
    amount_of_videos_to_review = 0
    amount_of_fellows = 0

    def __init__(self, amount_of_fellows, amount_of_videos_to_review):
        self.amount_of_videos_to_review = amount_of_videos_to_review
        self.amount_of_fellows = amount_of_fellows
        self.all_videos = [i for i in range(amount_of_fellows)]
        self.peer_review_scheme = [[] for i in range(amount_of_fellows)]

    # Get a video of fellow randomly, and remove that video from all video list so that it won't get picked again.
    @staticmethod
    def get_one_video_randomly(all_videos):
        if all_videos:
            choice = rchoice(all_videos)
            all_videos.remove(choice)
            return choice
        return None

    # Get the next index of fellow in current round assigning that should watch the video
    @staticmethod
    def get_next_index(curr_index, amount_of_fellows):
        next_index = (curr_index + 1) % amount_of_fellows
        return next_index

    # Get combination of videos for each fellow to watch
    def generate_scheme(self):
        # which fellow shall we start to give video to watch in next round of assigning
        index_fellow_to_watch_video = 0

        fail_to_generate_scheme = False

        # For all videos
        while self.all_videos:
            index_of_video = Scheme.get_one_video_randomly(self.all_videos)
            # to make sure each video will be watched by amount_of_videos_to_review times
            amount_of_video_need_be_assigned_curr_round = self.amount_of_videos_to_review
            # this check is used to prevent dead lock, because sometimes there will always one situation happen:
            # when the last video only have its owner to assign to
            # that case happen rarely so I tend to re-generate the scheme again
            check = 0

            while amount_of_video_need_be_assigned_curr_round > 0:
                check += 1

                if check >= self.amount_of_fellows:
                    fail_to_generate_scheme = True
                    break

                if index_of_video != index_fellow_to_watch_video \
                        and len(self.peer_review_scheme[index_fellow_to_watch_video]) < self.amount_of_videos_to_review:
                    # could assign video to this fellow
                    self.peer_review_scheme[index_fellow_to_watch_video].append(index_of_video)
                    amount_of_video_need_be_assigned_curr_round -= 1

                index_fellow_to_watch_video = Scheme.get_next_index(index_fellow_to_watch_video, self.amount_of_fellows)

        if fail_to_generate_scheme:
            return None

        return self.peer_review_scheme


def get_scheme(fellow_amount, amount_of_video_to_watch):
    scheme = None
    while not scheme:
        p = Scheme(fellow_amount, amount_of_video_to_watch)
        scheme = p.generate_scheme()

    return scheme
