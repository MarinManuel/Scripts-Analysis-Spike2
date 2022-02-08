* analysis_IFcurve_pulse.s2s
Ce script permet de plotter une courbe IF en réponse à des créneaux de courant dépolarisants.
-Lancer le script sur un fichier de données (.smr)
-Rentrer les informations nécessaires dans la boite de dialogue qui s'affiche
  --S'il n'existe pas de channel contenant la fréquence instantanée des spikes, cocher la case "Create frequency channel". Un nouveau Memory Channel, appelé "Freq" sera alors créé.
  --Pour éviter de prendre en compte les pulses au cours desquels l'intensité du courant a changé, cocher la case "Filter pulses for change in current amplitude". Un nouveau Level Channel, portant le même nom que celui sélectionné dans la case "Pulse Event" sera alors créé.
  --Le script permet de plotter la fréquence moyenne, mesure sur un certain pourcentage de la durée du pulse (default, 75%) en partant de la fin du pulse pour ne pas mesurer la période d'adaptation.
  --s'il l'on préfère plotter un ISI précis (par ex, 1er interval inter-spike), décocher la case "Plot stationary frequency" et choisir l'ISI désiré dans la boite "Plot ISI n°"
-Cliquer sur OK
-Le script affiche les pulses successivement, et demande de valider la zone de mesure.
-Une fois tous les pulses passés en revue (ou si la touche "Yes to all" a été pressée) la courbe IF est affichée. Chaque point représente un pulse.

* analysis_IFcurve_ramp.s2s
Ce script permet de plotter une courbe IF en réponse à une rampe de courant. Il mesure également:
  -les fréquences de recrutement et de dérecrutement
  -le seuil en voltage du premier potentiel d'action
  -la pente de la courve IF
-Lancer le script sur un fichier de données (.smr)
-Rentrer les informations nécessaires dans la boite de dialogue qui s'affiche
-le script propose de sauvegarder la courbe IF générée.
-les valeurs numériques sont affichées sous forme de curseurs dans le fichier de données, et sont écrites dans le fichier Log.
-3 valeurs de gains sont mesurées:
  --le gain ascendant ("ascSlope"), calculé sur toute la durée de la branche ascendante
  --le gain descendant ("descSlope"), calculé sur toute la durée de la branche descendante
  --le gain global ("Slope"), calculé sur l'ensemble de la rampe

* analysis_IVcurve.s2s
Ce script plot la courbe IV en réponse à une rampe de courant en voltage clamp
Une fois la courbe brute plottée, il estime le potentiel d'activation du PIC (point de pente nulle), et propose une région sur laquelle faire l'estimation de la conductance de fuite. Celle-ci est alors soustraite pour obtenir la courbe "leak-substracted" sur laquelle est estimée l'amplitude du PIC.
Appuyer sur "Accept" pour sauvegarder les fichiers de résultats. Le script écrira dans le Log les valeurs qu'il a estimé automatiquement que si l'utilisateur répond "Yes" à la question "Accept estimated values?". Dans la négative, seule les valeurs que l'utilisateur a mesuré lui-même en changeant la position des curseurs seront écrits dans le Log.

* analysis_spike.s2s
Ce script mesure différents paramètres sur un spike généré par un pulse de courant dépolarisant bref. Il se lance sur un fichier moyenné (.srf).
il mesure les paramètres suivants:
  -- RMP
  -- Spike height
  -- Spike half-width
  -- AHP Amplitude
  -- AHP Time-to-peak
  -- AHP Duration
  -- AHP 1/2 relaxation time
  -- AHP time constant
NB: pour aider le script à trouver le pic de l'AHP, en particulier lorsqu'il y a beaucoup de bruit, il est possible de zoomer sur l'AHP pour supprimer toute la région en fin d'AHP où le potentiel est revenu à la valeur de repos

* analysis_Accomodation.s2s
ce script mesure le seuil en voltage des potentiels d'action (voltage ou la vitesse d'évolution du potentiel dépasse 10mV/ms) et le plot sur un graphique en fonction du courant injecté.
Marche sur n'importe quel type de fichier de donnée (.smr).

* analysis_ZAP.s2s
ce script mesure l'impédance d'un MN en réponse à un courant sinusoidal de fréquence croissante (ZAP).
Le script se lance sur un fichier moyenné (.srf) contenant au moins la moyenne du potentiel de membrane et du courant injecté. Pour avoir plusieurs channels moyennés en même temps, sélectionner les channels d'intérêt (Ctrl+Click) avant de lancer la procédure de moyennage. Dans la boite de dialogue de moyennage, dans la liste "Channels", sélectionner "Selected:". Puis faire la moyenne comme d'habitude.
Le script plotte le module de l'impédance |Z|=FFT(Vm)/FFT(Im) entre les fréquences choisies dans la boite de dialogue. Il peut également lisser le résultat, en calculant une moyenne flottante sur un nombre de points choisi dans la boite de dialogue. Dans ce cas, le script estime la valeur de la fréquence de résonance et calcule la Qualité de la résonance. Ces valeurs sont reportées dans le log. 