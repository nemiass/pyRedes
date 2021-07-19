import json
import re
import os


def mask_to_decimal(mask: int) -> str:
    mask_binary = []
    mask_tmp = ""
    for i in range(1, 33):
        mask_tmp += "1" if i <= mask else "0"
        if i % 8 == 0:
            mask_binary.append(mask_tmp[i - 8: i])
    return ".".join([str(int(octeto, 2)) for octeto in mask_binary])


class Routing:
    # ToDo
    pass


class Router:
    # ToDo
    def __init__(self):
        pass


class Red:
    # ToDo
    def __init__(self):
        self.routers = {}


class PyRedes:
    def __init__(self):
        self.path_file = os.path.dirname(os.path.abspath(__file__))
        self.red = Red()

    def start(self):
        while True:
            print(" Pyredes by https://github.com/nemiass ".center(60, "*"))
            print("[1] - generar modelo\n[2] - enrrutar\n[3] - <salir>")
            opcion = input(">>>").strip()
            if opcion == "1":
                self.generar_modelo()
            elif opcion == "2":
                self.enrrutar()
            elif opcion == "3":
                break
            input("[enter continuar...]")
            # limpiar pantalla para windows
            os.system("cls")

    def generar_modelo(self):
        while True:
            print("cantidad de routers:")
            num_routers = input(">>>").strip()
            if re.match('[0-9]', num_routers):
                break
        if os.path.exists(f"{self.path_file}/config.json"):
            print("El archivo ya existe, ¡¡desea reemplazarlo!! [s/n]")
            opcion = input(">>>").strip()
            if opcion == "s":
                self.generar_model_json(int(num_routers))
            elif opcion == "n":
                print("`config.json` no fue modificado!")
            else:
                print("niguna opción seleccionada, regresando al inicio...")
                return
        else:
            self.generar_model_json(int(num_routers))

    def generar_model_json(self, n_r: int):
        model_json = {"Conf.Genrales": {
            "Interfaces": {
                "interfaz-lan": "gigabitEthernet",
                "interfaz-wan": "serial"
            }
        }}
        list_routers = []
        indices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        with open(f"{self.path_file}/config.json", "w", encoding="utf-8") as f:
            for i in range(n_r):
                model = {
                    f"{indices[i]}": {
                        "Area": "",
                        "Vecinos": "",
                        "Interfaces": {
                            "lan": {
                                "ip-red": "",
                                "puertos:": [
                                    ""
                                ]
                            },
                            "wan": {
                                "ip-red": "",
                                "puertos": [
                                    ""
                                ]
                            }
                        }
                    }
                }
                list_routers.append(model)
            model_json["Routers"] = list_routers
            json.dump(model_json, f, indent=4)
        print("Modelos generados correctamente `config.json`")

    def load_json_model(self):
        if os.path.exists(f"{self.path_file}/config.json"):
            with open(f"{self.path_file}/config.json", "r", encoding="utf-8") as f:
                json_model = json.load(f)
                print(json_model)
                # ToDo
                return 1
        print("No existe el archivo `config.json`")
        return 0

    def enrrutar(self):
        if not self.load_json_model():
            return

        while True:
            print("Enrrutamiento:")
            print("[1] - estatico\n[2] - rip v1\n[3] - ospf\n[4] - eigrp\n[5] - bgp\n[6] - <salir>")
            opcion = input(">>>").strip()

            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                break
            else:
                break


if __name__ == "__main__":
    pr = PyRedes()
    pr.start()
