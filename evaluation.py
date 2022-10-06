import json


class Evaluator:
    def __init__(self, path):
        with open(path, 'r') as j:
            sums = json.loads(j.read())
            self.combo: dict = sums["sticker"]["combo"]
            self.rarity: dict = sums["sticker"]["rarity"]
            self.origin: dict = sums["sticker"]["origin"]
            self.players: list = sums["player_god"]
            self.teams: list = sums["team_god"]

    def get_score(self, item):
        overpay = float(item["overpay"]["stickers"])
        stickers = item["stickers"]
        count = dict()
        avg_weight = 0

        for sticker in stickers:
            try:
                count[sticker] += 1
            except:
                count[sticker] = 1

        for sticker in count.keys():
            avg_weight += self.calculate_weight(count[sticker], sticker)

        avg_weight /= len(stickers)

        return avg_weight / overpay

    def calculate_weight(self, count, name: str):
        name = name.lower()
        combo_weight = float(self.combo[f"{count}x"])
        rarity_weight = float(self.rarity["paper"])
        origin_weight = float(self.origin["default"])

        for key in self.rarity.keys():
            if name.find(key) != -1:
                rarity_weight = float(self.rarity[key])
                break

        if name.find('20') != -1:
            if any([name.find(player) != -1 for player in self.players]):
                origin_weight = float(self.origin["player_god"])
            elif any([name.find(team) != -1 for team in self.teams]):
                origin_weight = float(self.origin["team_god"])
            else:
                origin_weight = float(self.origin["player"])

        weight = combo_weight * rarity_weight * origin_weight
        return weight
