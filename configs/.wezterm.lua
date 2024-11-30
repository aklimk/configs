local wezterm = require('wezterm')

local config = wezterm.config_builder()

config.enable_wayland = true
config.font_size = 11
config.color_scheme = "carbonfox"
config.hide_tab_bar_if_only_one_tab = true
config.unicode_version = 14
return config
