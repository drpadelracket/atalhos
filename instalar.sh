#!/bin/bash
# Liga este repositorio ao Espanso e mantem-no atualizado sozinho (git pull de 10 em 10 minutos).
# Correr uma vez em cada Mac, depois de clonar o repositorio para a pasta match do Espanso.
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
MATCH="$(dirname "$DIR")"
PLIST="$HOME/Library/LaunchAgents/com.drpadel.atalhos.plist"

# Limpa a ligacao antiga (versao com pasta DrPadel-Atalhos), se existir
if [ -L "$MATCH/drpadel.yml" ]; then
  rm "$MATCH/drpadel.yml"
fi

mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.drpadel.atalhos</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/git</string>
    <string>-C</string>
    <string>$DIR</string>
    <string>pull</string>
    <string>--ff-only</string>
    <string>-q</string>
  </array>
  <key>StartInterval</key>
  <integer>600</integer>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
EOF

launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"

echo ""
echo "Pronto. Atalhos Dr. Padel ligados ao Espanso."
echo "Experimenta escrever ;portal e carregar em espaco."
echo "Atualizam-se sozinhos de 10 em 10 minutos."
