from insta_follower import InstaFollower

# Dados do Instagram do usuário.
INSTAGRAM_USER = "YOUR INSTAGRAM USER"
INSTAGRAM_PASSWORD = "YOUR INSTAGRAM PASSWORD"

# Usuário do Instagram que possui seguidores a serem seguidos.
SIMILAR_ACCOUNT = "SIMILAR ACCOUNT"

# Cria uma instância da classe InstaFollower.
bot = InstaFollower(user=INSTAGRAM_USER, password=INSTAGRAM_PASSWORD, similar_account=SIMILAR_ACCOUNT)

# Realiza login.
bot.login()
# Procura os seguidores da conta.
bot.find_followers()
# Segue as contas.
bot.follow()
