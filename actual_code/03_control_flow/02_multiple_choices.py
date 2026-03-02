experiment = input("Which CERN experiment are you interested in? ").lower().strip()

if experiment == "atlas":
  print("General-purpose detectors at the LHC.")
elif experiment == "alice":  # elif is a contraction of "else if"
  print("Heavy-ion collisions and quark-gluon plasma.")
elif experiment == "cms":
  print("Compact Muon Selenoid")
elif experiment.startswith("lhc") and experiment.find("upgrade") > 0:
  print("High-luminosity LHC")
else:
  print("I don't know that experiment.")