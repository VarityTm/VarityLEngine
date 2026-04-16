#define MyAppName "VarityEngine"
#define MyAppVersion "1.0"
#define MyAppPublisher "VarityTeam"
#define MyAppExeName "VarityEngine.exe"
; Твой путь к папке проекта (проверь, что имя пользователя 'Урал' и папка 'VarityManager')
#define MyProjectDir "D:\Users\Урал\Desktop\Програмирование\VarityLManager"

[Setup]
AppId={{VarityEngine-Project-2026}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Если иконка не найдена, поставь ; перед строкой ниже
SetupIconFile="{#MyProjectDir}\icon.ico"
Compression=lzma
SolidCompression=yes
WizardStyle=modern
OutputDir={#MyProjectDir}
OutputBaseFilename=VarityEngine_Setup

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#MyProjectDir}\main.exe"; DestDir: "{app}"; DestName: "{#MyAppExeName}"; Flags: ignoreversion
Source: "{#MyProjectDir}\ИНСТРУКЦИЯ.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
; --- СКРИПТ ПРИВЯЗКИ ФАЙЛОВ .VAR ---
Root: HKA; Subkey: "Software\Classes\.var"; ValueType: string; ValueName: ""; ValueData: "VarityFile"; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\VarityFile"; ValueType: string; ValueName: ""; ValueData: "Сценарий Varity"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\VarityFile\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\VarityFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Run]
Filename: "{app}\ИНСТРУКЦИЯ.txt"; Description: "Открыть инструкцию"; Flags: postinstall shellexec skipifsilent