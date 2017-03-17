#!/usr/bin/env python3
running = True
while running:  

  import skilstak.colors as c
  import random
  import time
  total_p = 0
  total_c = 0
  first_time = True
  last_cards = ['None','None','None','None','None','None','None','None']
  cards_per_pack = 5
  roll_min = 1
  roll_max = 10000
  auto_time = 0
  auto_left = 0
  pack_pref = ''

  def cardroll(pack,rarity,golden,last_cards,not_debug=True):
    classic_l = ["Al'Akir the Windlord", "Alexstrasza", "Archmage Antonidas", "Baron Geddon", "Bloodmage Thalnos", "Cairne Bloodhoof", "Captain Greenskin", "Cenarius", "Deathwing", "Edwin VanCleef", "Grommash Hellscream", "Gruul", "Harrison Jones", "Hogger", "Illidan Stormrage", "King Krush", "King Mukla", "Leeroy Jenkins", "Lord Jaraxxus", "Lorewalker Cho", "Malygos", "Millhouse Manastorm", "Nat Pagle", "Nozdormu", "Onyxia", "Prophet Velen", "Ragnaros the Firelord", "Sylvanas Windrunner", "The Beast", "The Black Knight", "Tinkmaster Overspark", "Tirion Fordring", "Ysera"]
    classic_e = ["Southsea Captain", "Murloc Warleader", "Ancient of Lore", "Ancient of War", "Big Game Hunter", "Blood Knight", "Cabal Shadow Priest", "Doomsayer", "Earth Elemental", "Faceless Manipulator", "Kidnapper", "Molten Giant", "Mountain Giant", "Patient Assassin", "Sea Giant", "Pit Lord", "Hungry Crab", "Avenging Wrath", "Bane of Doom", "Bestial Wrath", "Brawl", "Doomhammer", "Far Sight", "Force of Nature", "Gladiator's Longbow", "Gorehowl", "Ice Block", "Lay on Hands", "Mindgames", "Preparation", "Pyroblast", "Shadowform", "Shield Slam", "Snake Trap", "Spellbender", "Sword of Justice", "Twisting Nether"]
    classic_r = ["Abomination", "Alarm-o-Bot", "Aldor Peacekeeper", "Ancestral Spirit", "Ancient Mage", "Ancient Watcher", "Angry Chicken", "Arcane Golem", "Argent Commander", "Armorsmith", "Auchenai Soulpriest", "Azure Drake", "Bite", "Blade Flurry", "Blessed Champion", "Blizzard", "Bloodsail Corsair", "Coldlight Oracle", "Coldlight Seer", "Commanding Shout", "Counterspell", "Crazed Alchemist", "Defender of Argus", "Demolisher", "Divine Favor", "Doomguard", "Eaglehorn Bow", "Emperor Cobra", "Equality", "Ethereal Arcanist", "Explosive Shot", "Felguard", "Feral Spirit", "Flare", "Frothing Berserker", "Gadgetzan Auctioneer", "Headcrack", "Holy Fire", "Holy Wrath", "Imp Master", "Injured Blademaster", "Keeper of the Grove", "Kirin Tor Mage", "Knife Juggler", "Lava Burst", "Lightning Storm", "Lightwarden", "Lightwell", "Mana Addict", "Mana Tide Totem", "Mana Wraith", "Mass Dispel", "Master Swordsmith", "Master of Disguise", "Mind Control Tech", "Misdirection", "Mortal Strike", "Murloc Tidecaller", "Nourish Rare", "Perdition's Blade", "Pint-Sized Summoner", "Questing Adventurer", "Ravenholdt Assassin", "SI:7 Agent", "Savagery", "Savannah Highmane", "Secretkeeper", "Shadow Madness", "Shadowflame", "Siphon Soul", "Stampeding Kodo", "Starfall", "Sunfury Protector", "Sunwalker", "Twilight Drake", "Upgrade!", "Vaporize", "Violet Teacher", "Void Terror", "Wild Pyromancer", "Young Priestess"]
    classic_c = ["Abusive Sergeant", "Acolyte of Pain", "Amani Berserker", "Ancient Brewmaster", "Arathi Weaponsmith", "Argent Protector", "Argent Squire", "Battle Rage", "Betrayal", "Blessing of Wisdom", "Blood Imp", "Bloodsail Raider", "Circle of Healing", "Cold Blood", "Conceal", "Cone of Cold", "Cruel Taskmaster",    "Cult Master", "Dark Iron Dwarf", "Deadly Shot", "Defias Ringleader", "Demonfire", "Dire Wolf Alpha", "Dread Corsair", "Druid of the Claw", "Dust Devil", "Earth Shock", "Earthen Ring Farseer", "Eviscerate", "Explosive Trap", "Eye for an Eye", "Faerie Dragon", "Fen Creeper", "Flame Imp", "Flesheating Ghoul", "Forked Lightning", "Freezing Trap", "Frost Elemental", "Harvest Golem", "Ice Barrier", "Ice Lance", "Inner Fire", "Inner Rage", "Ironbeak Owl", "Jungle Panther", "Leper Gnome", "Lightning Bolt", "Lightspawn", "Loot Hoarder", "Mad Bomber", "Mana Wyrm", "Mark of Nature", "Mirror Entity", "Mogu'shan Warden", "Naturalize", "Noble Sacrifice", "Power Overwhelming", "Power of the Wild", "Priestess of Elune", "Raging Worgen", "Rampage", "Redemption", "Repentance", "Scarlet Crusader", "Scavenging Hyena", "Sense Demons", "Shadowstep", "Shieldbearer", "Silence", "Silver Hand Knight", "Silvermoon Guardian", "Slam", "Snipe", "Sorcerer's Apprentice", "Soul of the Forest", "Southsea Deckhand", "Spellbreaker", "Spiteful Smith", "Stormforged Axe", "Stranglethorn Tiger", "Summoning Portal", "Tauren Warrior", "Temple Enforcer", "Thoughtsteal", "Thrallmar Farseer", "Unbound Elemental", "Unleash the Hounds", "Venture Co. Mercenary", "Windfury Harpy", "Wisp", "Worgen Infiltrator", "Wrath", "Young Dragonhawk", "Youthful Brewmaster"]

    gnomes_l = ["Blingtron 3000", "Bolvar Fordragon", "Dr. Boom", "Flame Leviathan", "Foe Reaper 4000", "Gahz'rilla", "Gazlowe", "Hemet Nesingwary", "Iron Juggernaut", "Mal'Ganis", "Malorne", "Mekgineer Thermaplugg", "Mimiron's Head", "Mogor the Ogre", "Neptulon", "Sneed's Old Shredder", "Toshley", "Trade Prince Gallywix", "Troggzor the Earthinator", "Vol'jin"]
    gnomes_e = ["Ancestor's Call", "Anima Golem", "Bouncing Blade", "Clockwork Giant", "Coghammer", "Cogmaster's Wrench", "Crush", "Dark Wispers", "Demonheart", "Echo of Medivh", "Enhance-o Mechano", "Feign Death", "Fel Reaver", "Hobgoblin", "Junkbot", "Lightbomb", "Mini-Mage", "Piloted Sky Golem", "Quartermaster", "Recombobulator", "Sabotage", "Shadowbomber", "Siltfin Spiritwalker", "Steamwheedle Sniper", "Tree of Life", "Wee Spellstopper"]
    gnomes_r = ["Arcane Nullifier", "Bomb Lobber", "Call Pet", "Cobalt Guardian", "Dunemaul Shaman", "Fel Cannon", "Gnomish Experimenter", "Goblin Blastmage", "Goblin Sapper", "Grove Tender", "Illuminator", "Imp-losion", "Iron Sensei", "Jeeves", "Kezan Mystic", "King of Beasts", "Light of the Naaru", "Lil' Exorcist", "Madder Bomber", "Mech-Bear-Cat", "Metaltooth Leaper", "Mistress of Pain", "Muster for Battle", "Ogre Ninja", "One-eyed Cheat", "Powermace", "Recycle", "Scarlet", "Screwjank", "Shadowboxer", "Shieldmaiden", "Siege Engine", "Soot Spewer", "Target Dummy", "Unstable Portal", "Upgraded Repair Bot", "Vitality Totem"]
    gnomes_c = ["Annoy-o-Tron", "Anodized Robo Cub", "Antique Healbot", "Burly Rocw Trogg", "Clockwork Gnome", "Cobra Shot", "Cogmaster", "Crackle", "Darkbomb", "Druid of the Fang", "Explosive Sheep", "Flamecannon", "Floating Watcher", "Flying Machine", "Force-Tank MAX", "Gilblin Stalker", "Glaivezooka", "Gnomeregan Infantry", "Goblin Auto-Barber", "Lost Tallstrider", "Mechanical Yeti", "Mechwarper", "Micro Machine", "Ogre Brute", "Ogre Warmaul", "Piloted Shredder", "Puddlestomper", "Salty Dog", "Seal of Light", "Shielded Minibot", "Ship's Cannon", "Shrinkmeister", "Snowchugger", "Spider Tank", "Stonesplinter Trogg", "Tinker's Sharpsword Oil", "Tinkertown Technician", "Velen's Chosen", "Warbot", "Whirling Zap-o-matic"]

    grand_l = ["Acidmaw","Anub'arak","Aviana","Bolf Ramshield","Chillmaw","Confessor Paletress","Dreadscale", "Eadric the Pure", "Eydis Darkbane", "Fjola Lightbane", "Gormok the Impaler", "Icehowl", "Justicar Trueheart", "Nexus-Champion Saraad", "Rhonin", "Skycap'n Kragg", "The Mistcaller", "The Skeleton Knight", "Varian Wrynn", "Wilfred Fizzlebang"]
    grand_e = ["Arcane Blast","Astral Communion","Beneath the Grounds","Charged Hammer","Coldarra Drake","Confuse","Crowd Favorite","Dark Bargain","Dreadsteed","Elemental Destruction","Enter the Coliseum","Frost Giant","Garrison Commander","Grand Crusader","Kodorider","Lock and Load","Magnataur Alpha","Master of Ceremonies","Mulch","Mysterious Challenger","Poisoned Blade","Recruiter","Sea Reaver","Shadowfiend","Sideshow Spelleater","Stablemaster","Twilight Guardian"]
    grand_r = ["Alexstrasza's Champion", "Argent Lance", "Argent Watchman", "Armored Warhorse", "Ball of Spiders", "Burgle", "Coliseum Manager", "Competitive Spirit","Convert", "Cutpurse", "Darnassus Aspirant", "Draenei Totemcarver","Effigy","Fallen Hero","Fencing Coach","Fist of Jaraxxus","Healing Wave","Injured Kvaldir","King's Defender","Knight of the Wild","Light's Champion","Master Jouster","Mogor's Champion","Polymorph: Boar","Powershot","Ram Wrangler","Saboteur","Savage Combatant","Shady Dealer","Sparring Partner","Spawn of Shadows","Thunder Bluff Valiant","Tiny Knight of Evil","Tuskarr Jouster","Void Crusher","Wyrmrest Agent"]
    grand_c = ["Ancestral Knowledge", "Argent Horserider", "Bash", "Bear Trap", "Bolster", "Boneguard Lieutenant", "Brave Archer", "Buccaneer", "Captured Jormungar", "Clockwork Knight", "Dalaran Aspirant", "Demonfuse", "Dragonhawk Rider", "Druid of the Saber", "Evil Heckler", "Fearsome Doomguard", "Flame Juggler", "Flame Lance", "Flash Heal", "Frigid Snobold", "Gadgetzan Jouster", "Holy Champion", "Ice Rager", "King's Elekk", "Kvaldir Raider", "Lance Carrier", "Living Roots", "Lowly Squire", "Maiden of the Lake", "Mukla's Champion", "Murloc Knight", "North Sea Kraken", "Orgrimmar Aspirant", "Pit Fighter", "Power Word: Glory", "Refreshment Vendor", "Seal of Champions", "Shado-Pan Rider", "Silent Knight", "Silver Hand Regent", "Spellslinger", "Totem Golem", "Tournament Attendee", "Tournament Medic", "Tuskarr Totemic", "Undercity Valiant", "Warhorse Trainer", "Wildwalker", "Wrathguard"]

    gods_l = [""]
    gods_e = [""]
    gods_r = [""]
    gods_c = [""]

    if not_debug:
      if pack == 'c':
        if rarity == 'l':
          card = random.choice(classic_l)
          effect = c.yellow
        elif rarity == 'e':
          card = random.choice(classic_e)
          effect = c.violet
        elif rarity == 'r':
          card = random.choice(classic_r)
          effect = c.blue
        elif rarity == 'c':
          card = random.choice(classic_c)
          effect = c.base3

      elif pack == 'g':
        if rarity == 'l':
          card = random.choice(gnomes_l)
          effect = c.yellow
        elif rarity == 'e':
          card = random.choice(gnomes_e)
          effect = c.violet
        elif rarity == 'r':
          card = random.choice(gnomes_r)
          effect = c.blue
        elif rarity == 'c':
          card = random.choice(gnomes_c)
          effect = c.base3

      elif pack == 't':
        if rarity == 'l':
          card = random.choice(grand_l)
          effect = c.yellow
        elif rarity == 'e':
          card = random.choice(grand_e)
          effect = c.violet
        elif rarity == 'r':
          card = random.choice(grand_r)
          effect = c.blue
        elif rarity == 'c':
          card = random.choice(grand_c)
          effect = c.base3

      elif pack == 'g':
        if rarity == 'l':
          card = random.choice(gods_l)
          effect = c.yellow
        elif rarity == 'e':
          card = random.choice(gods_e)
          effect = c.violet
        elif rarity == 'r':
          card = random.choice(gods_r)
          effect = c.blue
        elif rarity == 'c':
          card = random.choice(gods_c)
          effect = c.base3

      if rarity == 'c':
        if golden == '':
          last_cards.pop(0)
          last_cards.insert(0,card)
        else:
          last_cards.pop(1)
          last_cards.insert(1,card)
      elif rarity == 'r':
        if golden == '':
          last_cards.pop(2)
          last_cards.insert(2,card)
        else:
          last_cards.pop(3)
          last_cards.insert(3,card)
      elif rarity == 'e':
        if golden == '':
          last_cards.pop(4)
          last_cards.insert(4,card)
        else:
          last_cards.pop(5)
          last_cards.insert(5,card)
      elif rarity == 'l':
        if golden == '':
          last_cards.pop(6)
          last_cards.insert(6,card)
        else:
          last_cards.pop(7)
          last_cards.insert(7,card)
      result = golden + effect + card
      return [last_cards,result]
    else:
        if pack == 'c':
          if rarity == 'l':
            if golden == 'add':
              classic_l.append(last_cards)
            else:
              classic_l.remove(last_cards)
          elif rarity == 'e':
            if golden == 'add':
              classic_e.append(last_cards)
            else:
              classic_e.remove(last_cards)
          elif rarity == 'r':
            if golden == 'add':
              classic_r.append(last_cards)
            else:
              classic_r.remove(last_cards)
          elif rarity == 'c':
            if golden == 'add':
              classic_c.append(last_cards)
            else:
              classic_c.remove(last_cards)
        elif pack == 'g':
          if rarity == 'l':
            if golden == 'add':
              gnomes_l.append(last_cards)
            else:
              gnomes_l.remove(last_cards)
          elif pack == 'e':
            if golden == 'add':
              gnomes_e.append(last_cards)
            else:
              gnomes_e.remove(last_cards)
          elif pack == 'r':
            if golden == 'add':
              gnomes_r.append(last_cards)
            else:
              gnomes_r.remove(last_cards)
          elif pack == 'c':
            if golden == 'add':
              gnomes_c.append(last_cards)
            else:
              gnomes_c.remove(last_cards)
        elif pack == 't':
          if rarity == 'l':
            if golden == 'add':
              grand_l.append(last_cards)
            else:
              grand_l.remove(last_cards)
          elif rarity == 'e':
            if golden == 'add':
              grand_e.append(last_cards)
            else:
              grand_e.remove(last_cards)
          elif rarity == 'r':
            if golden == 'add':
              grand_r.append(last_cards)
            else:
              grand_r.remove(last_cards)
          elif rarity == 'c':
            if golden == 'add':
              grand_c.append(last_cards)
            else:
              grand_c.remove(last_cards)

  def prob(commons,golden,stats,cards_per_pack,roll_min,roll_max):
      while True:
          rare_roll = random.randint(roll_min,roll_max)
          if rare_roll >= 1 and rare_roll <= 94: 
              if rare_roll >= 1 and rare_roll <= 7:
                golden = c.yellow + 'Golden '
                g_l = stats.pop(7)
                g_l += 1
                stats.insert(7,g_l)
              else:
                l = stats.pop(6)
                l += 1
                stats.insert(6,l) 
              rarity = 'l'
          elif rare_roll >= 95 and rare_roll <= 502:
              if rare_roll >= 95 and rare_roll <= 114:
                golden = c.yellow + 'Golden '
                g_e = stats.pop(5)
                g_e += 1
                stats.insert(5,g_e)
              else:
                e = stats.pop(4)
                e += 1
                stats.insert(4,e)
              rarity = 'e' 
          elif rare_roll >= 503 and rare_roll <= 2662:
              if rare_roll >= 503 and rare_roll <= 630:
                  golden = c.yellow + 'Golden '
                  g_r = stats.pop(3)
                  g_r += 1
                  stats.insert(3,g_r)
              else:
                r = stats.pop(2)
                r += 1
                stats.insert(2,r)
              rarity = 'r'
          elif rare_roll >= 2663 and rare_roll <= 9698:
              if cards_per_pack == commons+1:
                continue
              if rare_roll >= 2663 and rare_roll <= 2811:
                  golden = c.yellow + 'Golden '
                  g_c = stats.pop(1)
                  g_c += 1
                  stats.insert(1,g_c)
              else:
                com = stats.pop(0)
                com += 1
                stats.insert(0,com)
              rarity = 'c'
              commons +=  1
          else:
            continue
          break
      return [stats,rarity,commons,golden]


  def percentage(stat,total_p,cards_per_pack,total_c):
    if total_p == 0:
      return '  (0.0000%)'
    else:
      percent_uncut = (stat/(total_c)) * 100
      return '  (' + (str(percent_uncut) + '0000')[:6] + '%)'
  # Commons, golden commons, rares, golden rares, epics, golden epics, legendaries, golden legendaries
  stats = [0,0,0,0,0,0,0,0]

  while True:
      print(c.clear,end='')
      if first_time:
        print('_______________\n_______________\n_______________\n_______________\n_______________\n')
        print(c.base3+'Welcome, what pack do you want to open?\n'+c.orange+'[C] Classic\n'+c.red+'[G] Goblins vs Gnomes\n'+c.magenta+'[T] The Grand Tournament\n' + c.base00 + '[W] Comming soon: Whispers of Old Gods\n' + c.green + '[E] Exit\n'+c.base3+'Anything else put will open a random pack.\n\n')
      else:
        for order in range(cards_per_pack):
          print(cards.pop(random.randint(0,cards_per_pack_poploop-order)-1))
        print()
      first_time = True
      cost = 0
      math_p = total_p
      while True:
          if math_p >= 60:
              math_p -= 60
              cost += 70
          elif math_p >= 40:
              math_p -= 40
              cost += 50
          elif math_p >= 15:
              math_p -= 15
              cost += 20
          elif math_p >= 7:
              math_p -= 7
              cost += 10

          elif math_p >= 2:
              math_p -= 2
              cost += 3
          elif math_p == 1:
              cost += 3
              break
          elif math_p == 0:
              break
      countstat = 0
      dust = 0
      for stat in stats:
        last_this = last_cards.pop(countstat)
        last_cards.insert(countstat,last_this)
        last_this = '(Last card: ' + last_this + ')'
        printstats = str(stat) + percentage(stat,total_p,cards_per_pack,total_c) + '   ' + last_this
        if countstat == 0:
          print(c.base3 + 'Commons:            ' + printstats)
          dust += stat * 5 
        elif countstat == 1:
          print(c.yellow + 'Golden ' + c.base3 + 'Commons:     ' + printstats)
          dust += stat * 50
        elif countstat == 2:
          print(c.blue + 'Rares:              ' + printstats)
          dust += stat * 20
        elif countstat == 3:
          print(c.yellow + 'Golden ' + c.blue + 'Rares:       ' + printstats)
          dust += stat * 100
        elif countstat == 4:
          print(c.violet + 'Epics:              ' + printstats)
          dust += stat * 100
        elif countstat == 5:
          print(c.yellow + 'Golden '+ c.violet + 'Epics:       ' + printstats)
          dust += stat * 400
        elif countstat == 6:
          print(c.yellow + 'Legendaries:        ' + printstats)
          dust += stat * 400
        elif countstat == 7:
          print(c.yellow + 'Golden Legendaries: ' + printstats)
          dust += stat * 1600
          print()
          print(c.orange + 'Total Packs:        ' + str(total_p) + '  (Total Cards: ' + str(total_c) + ')')
          print(c.green + 'Total Money Spent: ' + '$' + str(cost))
          if cost == 0:
            print(c.cyan + 'Total Dust: 0/$ (' + str(dust) + ' Total, 0/pack)')
          else:
            print(c.cyan + 'Total Dust: ' + str(round(dust/cost)) + '/$ (' + str(dust) + ' Total, ' + str(round(dust/total_p)) + '/pack)')
        countstat += 1
      print()
      if auto_left >= 1:
        print(c.base3+'>>> ',end='')
        time.sleep(auto_time)
        auto_left -= 1
        pack = pack_pref
      else:
        try:
          pack = input(c.base3+'>>> ').strip().lower()
        except KeyboardInterrupt:
          running = False
          break
      print(c.clear,end='')
      if pack == '<>debug numbers<>':
        cards_per_pack = int(input('Cards per pack.\n>>> '))
        if cards_per_pack <= 0:
          cards_per_pack = 5
        roll_min = int(input('Min. number roll for rarity.\n>>> '))
        roll_max = int(input('Max. number roll for rarity.\n>>> '))
        if roll_max < roll_min or roll_max <= 0 or roll_min <= 0 or roll_min >= 2663:
          roll_max = 10000
          roll_min = 1
        continue
      elif pack == '<>debug reset<>':
        break
      elif pack == 'e':
        running = False
        break
      elif pack == '<>debug auto<>':
        auto_left = int(input('Packs to open.\n>>> '))
        auto_time = float(input('Time inbetween openings.\n>>> '))
        pack_pref = input('Pack Prefference.\n>>> ')
        if auto_time < 0:
          auto_time = 0
        continue
      elif pack == '<>debug cardchange<>':
        add_or_remove = input('Adding or removing (Add, Remove)\n>>> ').strip().lower()
        packtype = input('Pack type (C, G, or T).\n>>> ').strip().lower()
        cardrarity = input('Rarity (L, E, R, or C).\n>>> ').strip().lower()
        cardname = input('Card name.\n>>> ')
        cardroll(packtype,cardrarity,add_or_remove,cardname,not_debug=False)
        continue
      print(c.clear,end='')
      total_p += 1
      total_c += cards_per_pack 
      if pack != 'c' and pack != 'g' and pack != 't':
          pack = random.choice(['c','g','t'])
      commons = 0
      cards = []
      for count in range(cards_per_pack):
          rarity = None
          golden = ''

          returnlist = prob(commons,golden,stats,cards_per_pack,roll_min,roll_max)
          golden = returnlist.pop()
          commons = returnlist.pop()
          rarity = returnlist.pop()
          stats = returnlist.pop()

          result = cardroll(pack,rarity,golden,last_cards)
          cards.append(result.pop())
          last_cards = result.pop()
      cards_per_pack_poploop = cards_per_pack - 1
      first_time = False
  print(c.clear,end='')
print(c.clear,end='')
