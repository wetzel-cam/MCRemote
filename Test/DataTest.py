import Data

mcdata = Data.AdvancementData

print(list(mcdata.story_advancements))
print(mcdata.nether_advancements)
print(mcdata.end_advancements)
print(mcdata.custom_advancements)

print(mcdata.get_advancement(mcdata, 'story', 'root'))