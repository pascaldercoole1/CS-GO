import pymem
import pymem.process
import os
import time

dwEntityList = 0x4DFFF7C
dwGlowObjectManager = 0x535AA08
m_iGlowIndex = 0x10488
m_iTeamNum = 0xF4


def main():
    print("Loading Cheat...")

    pm = pymem.Pymem("csgo.exe")
    client = "?"

    os.system('cls')

    if pm:
        print("csgo found!")

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

        if client:
            print("client found! >", client)
        else:
            print("client not found!")


        time.sleep(1)

        os.system('cls')

        print("Loading ESP...")

        time.sleep(1)

        os.system('cls')

        print("dwEntityList:",dwEntityList)
        print("dwGlowObjectManager:",dwGlowObjectManager)
        print("m_iGlowIndex:",m_iGlowIndex)
        print("m_iTeamNum:",m_iTeamNum)

        print("ESP loaded!")

    else:
        print("csgo not found!")
        os.system("pause")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow


if __name__ == '__main__':
    main()
