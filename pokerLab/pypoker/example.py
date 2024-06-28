from Fish import FishPlayer
from Honest import HonestPlayer

from pypokerengine.api.game import setup_config, start_poker

config = setup_config(max_round=100, initial_stack=100, small_blind_amount=5)
config.register_player(name="h1", algorithm=HonestPlayer())
config.register_player(name="h2", algorithm=HonestPlayer())
config.register_player(name="f1", algorithm=FishPlayer())
game_result = start_poker(config, verbose=1)
