import json
# Obtain advancements info
# Obtain items info
# Obtain players info
# etc.


class AdvancementData:
    _advancements_data = json.loads(open('./Data/advancements.json').read())

    story_advancements = _advancements_data['story']
    nether_advancements = _advancements_data['nether']
    end_advancements = _advancements_data['end']
    custom_advancements = _advancements_data['custom']

    @staticmethod
    def _get_advancement_id(advancement):
        return advancement['id']

    @staticmethod
    def _get_advancement_namespace(advancement):
        return advancement['namespace']

    @staticmethod
    def get_advancement(category, advancement):
        if category == 'story':
            adv = AdvancementData.story_advancements[advancement]
        elif category == 'nether':
            adv = AdvancementData.nether_advancements[advancement]
        elif category == 'end':
            adv = AdvancementData.end_advancements[advancement]
        elif category == 'custom':
            adv = AdvancementData.custom_advancements[advancement]

        return adv

    @staticmethod
    def get_advancement_ingame_id(advancement):
        return AdvancementData._get_advancement_namespace(advancement) + ':' + \
               AdvancementData._get_advancement_id(advancement)

class ItemData:
    pass


class PlayerData:
    pass
