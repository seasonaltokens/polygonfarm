from brownie import SeasonalTokenFarm, accounts

uniswap_v3_position_manager = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
spring_address = "0xf04aF3f4E4929F7CD25A751E6149A3318373d4FE"
summer_address = "0x4D4f3715050571A447FfFa2Cd4Cf091C7014CA5c"
autumn_address = "0x4c3bAe16c79c30eEB1004Fb03C878d89695e3a99"
winter_address = "0xCcbA0b2bc4BAbe4cbFb6bD2f1Edc2A9e86b7845f"

start_date = 1641340800 # 2022-01-05 00:00:00 UTC

def main():
    acct = accounts.load('live-deployment')
    SeasonalTokenFarm.deploy(uniswap_v3_position_manager, 
                             spring_address,
                             summer_address,
                             autumn_address,
                             winter_address,
                             weth_address, 
                             start_date,
                             {'from': acct, 'priority_fee':"20 gwei"})
