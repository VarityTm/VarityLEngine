import os
import random
import sys

# Попытка импорта winsound только для Windows
try:
    import winsound
except ImportError:
    winsound = None

def run_varity(lines, file_dir=None):
    if file_dir:
        os.chdir(file_dir)
    
    vars = {}
    labels = {line.strip()[1:]: i for i, line in enumerate(lines) if line.strip().startswith(":")}
    pc = 0

    while pc < len(lines):
        line = lines[pc].strip()
        
        if not line or line.startswith(":") or line.startswith("-"):
            pc += 1
            continue

        parts = line.split(" ", 1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        try:
            if cmd == "показать":
                val = args.strip('"') if args.startswith('"') else vars.get(args.strip(), args.strip())
                print(val)
                pc += 1

            elif cmd == "переменная":
                name, val = args.split("=")
                vars[name.strip()] = eval(val, {}, vars)
                pc += 1

            elif cmd == "ввод":
                name, prompt = args.split("=")
                prompt_text = prompt.strip().strip('"')
                vars[name.strip()] = input(f"{prompt_text} ")
                pc += 1

            elif cmd == "очистить":
                os.system('cls' if os.name == 'nt' else 'clear')
                pc += 1

            elif cmd == "пауза":
                input("\nНажмите Enter, чтобы продолжить...")
                pc += 1

            elif cmd == "цвет":
                colors = {
                    "белый": "0", "красный": "31", "зеленый": "32", 
                    "желтый": "33", "синий": "34", "фиолетовый": "35", "стандарт": "0"
                }
                c_code = colors.get(args.strip().lower(), "0")
                print(f"\033[{c_code}m", end="")
                pc += 1

            elif cmd == "звук":
                if winsound:
                    winsound.Beep(750, 300)
                pc += 1

            elif cmd == "создать":
                os.makedirs(args.strip(), exist_ok=True)
                pc += 1

            elif cmd == "записать":
                content, filename_part = args.split(" в ")
                fname = vars.get(filename_part.strip(), filename_part.strip())
                text = content.strip('"') if content.startswith('"') else str(vars.get(content.strip(), content.strip()))
                with open(str(fname), "a", encoding="utf-8") as f:
                    f.write(text + "\n")
                pc += 1

            elif cmd == "шанс":
                name, range_part = args.split("=")
                r = range_part.replace(" до ", " ").split()
                vars[name.strip()] = random.randint(int(r[0]), int(r[1]))
                pc += 1

            elif cmd == "выбор":
                v_name = args.split("(")[0].strip()
                quest = args.split("(")[1].split(")")[0]
                opts = args.split(")")[-1].strip().split("|")
                print(f"\n{quest}")
                for i, o in enumerate(opts, 1):
                    print(f"{i}. {o.strip()}")
                ans = input("Ваш выбор: ")
                vars[v_name] = int(ans) if ans.isdigit() else ans
                pc += 1

            elif cmd == "если":
                sep = " то перейти " if " то перейти " in args else " то выполнить"
                cond_part, target = args.split(sep)
                sub_conds = cond_part.split(" и ")
                res = []
                for cond in sub_conds:
                    for op_w, op_s in [("больше", ">"), ("меньше", "<"), ("равно", "==")]:
                        if op_w in cond:
                            l, r = cond.split(op_w)
                            v_l = vars.get(l.strip(), 0)
                            v_r = vars.get(r.strip()) if r.strip() in vars else eval(r.strip())
                            res.append(eval(f"{v_l} {op_s} {v_r}"))
                            break
                
                if all(res):
                    if "выполнить" in sep: 
                        pc += 1
                    else: 
                        pc = labels.get(target.strip().strip(":"), pc + 1)
                else:
                    if "выполнить" in sep:
                        tmp = pc + 1
                        while tmp < len(lines) and not (lines[tmp].strip().startswith(":") or "перейти" in lines[tmp]):
                            tmp += 1
                        pc = tmp
                    else: 
                        pc += 1

            elif cmd == "перейти":
                pc = labels.get(args.strip().strip(":"), pc + 1)

            elif cmd == "стоп":
                break

            else:
                pc += 1
        
        except Exception as e:
            print(f"\033[31mОшибка в строке {pc+1}: {e}\033[0m")
            pc += 1
    
    print("\033[0m\n--- Программа завершена ---")
    input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, "r", encoding="utf-8") as f:
            run_varity(f.readlines(), os.path.dirname(file_path))
    else:
        files = [f for f in os.listdir('.') if f.endswith('.var')]
        if not files:
            print("Файлы .var не найдены.")
            input("Enter...")
        else:
            print("=== Батник для русс чайников: Выберите сценарий ===")
            for i, f in enumerate(files, 1): print(f"[{i}] {f}")
            try:
                ch = int(input("\nНомер: "))
                with open(files[ch-1], "r", encoding="utf-8") as f: run_varity(f.readlines())
            except: 
                print("Ошибка выбора!")
                input()