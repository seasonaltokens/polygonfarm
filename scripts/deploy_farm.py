from brownie import SeasonalTokenFarm, accounts

uniswap_v3_position_manager = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
weth_address = "0x64659Fa9064Bb434daA6E8e0b2706D01e9f9e30F"
spring_address = "0x96888C4e067fFDB57B107d50928c11b8Cbee2eC7"
summer_address = "0x88f257116f56Fb6E29D6EE89216207261ca900ca"
autumn_address = "0xb186082Dfb420F1CB675e77c074d5213538e1e4C"
winter_address = "0x0f73Da8D0F70e4eE9ba5e254634d8faA7c821875"

start_date = 1641340800 # 2022-01-05 00:00:00 UTC

def main():
    acct = accounts.load('deployment')
    SeasonalTokenFarm.deploy(uniswap_v3_position_manager, 
                             spring_address,
                             summer_address,
                             autumn_address,
                             winter_address,
                             weth_address, 
                             start_date,
                             {'from': acct, 'priority_fee':"2 gwei"})
