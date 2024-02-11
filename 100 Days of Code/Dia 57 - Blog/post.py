class Post:
    """
    Representa um post em um blog.
    """
    def __init__(self, post_id, title, subtitle, body):
        """
        Construtor da classe.
        :param post_id: Identificador único do post.
        :param title: Título do post.
        :param subtitle: Subtítulo do post.
        :param body: Corpo do post.
        """
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

