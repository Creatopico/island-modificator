# get
execute store result score DataVersion fktool run data get entity @r DataVersion

# set
scoreboard players set McVersion fktool 0
execute if score DataVersion fktool matches 3106.. run scoreboard players set McVersion fktool 11900
execute if score DataVersion fktool matches 3066..3105 run scoreboard players set McVersion fktool 11900
execute if score DataVersion fktool matches 2966..2975 run scoreboard players set McVersion fktool 11802
execute if score DataVersion fktool matches 2825..2865 run scoreboard players set McVersion fktool 11800
execute if score DataVersion fktool matches 2701..2730 run scoreboard players set McVersion fktool 11700
execute if score DataVersion fktool matches 2569..2586 run scoreboard players set McVersion fktool 11602
execute if score DataVersion fktool matches 2320..2567 run scoreboard players set McVersion fktool 11600
execute if score DataVersion fktool matches 2067..2230 run scoreboard players set McVersion fktool 11500
execute if score DataVersion fktool matches 1901..1976 run scoreboard players set McVersion fktool 11400
execute if score DataVersion fktool matches 1444..1631 run scoreboard players set McVersion fktool 11300
execute if score DataVersion fktool matches 1..1343 run scoreboard players set McVersion fktool 11200

# require
execute unless entity @p run tellraw @a {"text":"WARNING: a connected player is required to get the Minecraft version. Default setting : 1.19.0. Use /reload with a player ingame to update it.","color":"red"}
execute unless score DataVersion fktool matches 1.. run scoreboard players set DataVersion fktool -1
execute if entity @p if score DataVersion fktool matches -1 run tellraw @a {"text":"ERROR: DataVersion not recognized. Do you use intensive plugins, mods or optimized server type? Default setting : 1.19.0","color":"red"}
execute unless entity @p run scoreboard players set McVersion fktool 11900
