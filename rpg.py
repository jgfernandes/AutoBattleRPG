import threading
import time
import random
import sys

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.min_physical_damage = 1
        self.max_physical_damage = 10
        self.min_magical_damage = 1
        self.max_magical_damage = 10
        self.min_range_damage = 1
        self.max_range_damage = 10
        self.min_defense = 1
        self.max_defense = 10
        self.min_magic_defense = 1
        self.max_magic_defense = 10
        self.base_critical_chance = 0.1
        self.critical_damage = 2.0
        self.hp_regen = 1
        self.mana_regen = 1
        self.base_cooldown = 10
        
        self.action_bar = 0
        self.strenght = 10
        self.intelligence = 10
        self.luck = 10
        self.wisdom = 10
        self.agility = 10
        self.vitality = 10

    def physical_damage(self):
        return random.randint(self.min_physical_damage, self.max_physical_damage)

    def magical_damage(self):
        return random.randint(self.min_magical_damage, self.max_magical_damage)

    def range_damage(self):
        return random.randint(self.min_range_damage, self.max_range_damage)

    def defense(self):
        return random.randint(self.min_defense, self.max_defense)

    def magic_defense(self):
        return random.randint(self.min_magic_defense, self.max_magic_defense)

    def increase_hp(self):
        return self.vitality * 10

    def critical_chance(self):
        return random.random() < self.base_critical_chance

    def fill_action_bar(self):
        while True:
            while self.action_bar < 100:
                self.action_bar += 10
                time.sleep
    def action_cooldown(self):
        return self.base_cooldown - (self.agility * 0.1)

    def cast_spell(self, spell_name):
        if spell_name not in self.spells:
            print(f'{spell_name} is not a valid spell.')
            return
        spell = self.spells[spell_name]
        if self.mana < spell["mana_cost"]:
            print(f'{self.name} does not have enough mana to cast {spell_name}.')
            return
        self.mana -= spell["mana_cost"]
        if spell_name == "heal":
            heal_amount = spell["power"]()
            self.hp += heal_amount
            print(f'{self.name} cast {spell_name} and healed for {heal_amount}.')
        elif spell_name == "damage":
            damage = spell["power"]()
            self.hp -= damage
            print(f'{self.name} cast {spell_name} and dealt {damage} damage.')
        elif spell_name == "mana":
            mana_amount = spell["power"]()
            self.mana += mana_amount
            print(f'{self.name} cast {spell_name} and regained {mana_amount} mana.')

class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
    
    def start(self):
        thread1 = threading.Thread(target=self.character1.fill_action_bar)
        thread2 = threading.Thread(target=self.character2.fill_action_bar)
        thread1.start()
        thread2.start()
        while True:
            if self.character1.action_bar >= 100:
                damage = self.character1.physical_damage()
                if self.character1.critical_chance():
                    damage *= self.character1.critical_damage
                    print(f'{self.character1.name} landed a critical hit!')
                self.character2.hp -= damage
                print(f'{self.character1.name} dealt {damage} damage to {self.character2.name}.')
                print(f'{self.character2.name} HP: {self.character2.hp}')
                self.character1.action_bar = 0
                
            if self.character2.action_bar >= 100:
                damage = self.character2.physical_damage()
                if self.character2.critical_chance():
                    damage *= self.character2.critical_damage
                    print(f'{self.character2.name} landed a critical hit!')
                self.character1.hp -= damage
                print(f'{self.character2.name} dealt {damage} damage to {self.character1.name}.')
                print(f'{self.character1.name} HP: {self.character1.hp}')
                self.character2.action_bar = 0

            # Print the action points of each player every 0.1 seconds
            time.sleep(0.1)
            print(f'{self.character1.name} action points: {self.character1.action_bar}')
            print(f'{self.character2.name} action points: {self.character2.action_bar}')
            
            if self.character1.hp <= 0 or self.character2.hp <= 0:
                if self.character1.hp <= 0:
                    print(f'{self.character2.name} wins!')
                    
                else:
                    print(f'{self.character1.name} wins!')

                sys.exit()
                    
    
            

player1 = Character("Player 1")
player2 = Character("Player 2")

battle = Battle(player1, player2)
battle.start()