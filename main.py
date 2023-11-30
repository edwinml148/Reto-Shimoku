# from os import getenv
# import shimoku_api_python as Shimoku

# access_token = getenv('SHIMOKU_TOKEN')
# universe_id: str = getenv('UNIVERSE_ID')
# workspace_id: str = getenv('WORKSPACE_ID')

# # Client initialization with playground mode
# s = Shimoku.Client(
#     access_token=access_token,
#     universe_id=universe_id,
# )


from os import getenv
import shimoku_api_python as Shimoku

access_token = 'c5a33aee-4f96-4451-a2a2-28c193f1fd85'
universe_id: str = '271b8e52-b6a0-474d-88d4-045aef93cc40'
workspace_id: str = '214f2129-1303-4a93-8d13-5ee21158547f'

# Client initialization with playground mode
s = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
)