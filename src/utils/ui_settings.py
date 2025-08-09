class UISettings:
    """
    Utility class for managing UI settings.
    """
    @staticmethod
    def feedback(content: str, liked: bool = True):
        """
        Process user feedback on the generated response.

        Parameters:
            content (str): The content that was liked/disliked.
            liked (bool): Whether the user liked (True) or disliked (False) the response.
        """
        if liked:
            print("You upvoted this response: " + content[:100] + "...")
        else:
            print("You downvoted this response: " + content[:100] + "...")
