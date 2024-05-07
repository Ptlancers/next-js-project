#Bundle.nsi
Name "Receipt-Installer"

# Set the default installation directory
InstallDir "$PROGRAMFILES\Receipt"

# Request application privileges for Windows Vista and later
RequestExecutionLevel admin

# Define variables for file paths
Var Receipt
Var IndexBackend

# Define installation process
Section
  # Set output path to the installation directory
  SetOutPath $INSTDIR

  # Define variables for file paths using StrCpy within the Section
  StrCpy $Receipt "C:\Users\Administrator\Desktop\Projects\next-js-project\src-tauri\target\release\Receipt.exe"
  StrCpy $IndexBackend "C:\Users\Administrator\Desktop\Projects\next-js-project\api\dist\index.exe"

  # Install Receipt.exe
  File $Receipt

  # Install index.exe
  File $IndexBackend

  # Optionally, create shortcuts
  CreateShortCut "$DESKTOP\Receipt.lnk" "$INSTDIR\Receipt.exe" # Create shortcut on desktop
  CreateShortCut "$SMPROGRAMS\Receipt\Receipt.lnk" "$INSTDIR\Receipt.exe" # Create shortcut in Start Menu
SectionEnd

# output
; (rest of the output remains the same)