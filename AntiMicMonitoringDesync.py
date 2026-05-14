import obspython as obs

######## Global Variables ########
update_interval = 60

######## Config Variables ########
min_slider_value = 1
max_slider_value = 3600
slider_inverval = 1
default_update_interval = 60

######## Methods ########


def reset_monitoring():
  obs.obs_reset_audio_monitoring()
  print("Reset audio monitoring")


######## Main OBS functions ########


def script_defaults(settings):
  global default_update_interval
  obs.obs_data_set_default_int(
      settings, "update_interval", default_update_interval)


def script_update(settings):
  global update_interval
  update_interval = obs.obs_data_get_int(settings, "update_interval")
  obs.timer_remove(reset_monitoring)
  obs.timer_add(reset_monitoring, update_interval*1000)


def script_load(settings):
  global update_interval
  update_interval = obs.obs_data_get_int(settings, "update_interval")
  obs.timer_add(reset_monitoring, update_interval*1000)


def script_properties():
  props = obs.obs_properties_create()
  obs.obs_properties_add_int_slider(
      props, "update_interval", "Update Interval (s):", min_slider_value, max_slider_value, slider_inverval)

  return props


def script_description():
  return '<center><h2> Anti Mic Monitoring Desync</h2></center><center><h4>Original script: <a href="https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync">GitHub</a></h4></center>'
