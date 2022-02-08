* analysis_IFcurve_pulse.s2s
Ce script permet de plotter une courbe IF en r�ponse � des cr�neaux de courant d�polarisants.
-Lancer le script sur un fichier de donn�es (.smr)
-Rentrer les informations n�cessaires dans la boite de dialogue qui s'affiche
  --S'il n'existe pas de channel contenant la fr�quence instantan�e des spikes, cocher la case "Create frequency channel". Un nouveau Memory Channel, appel� "Freq" sera alors cr��.
  --Pour �viter de prendre en compte les pulses au cours desquels l'intensit� du courant a chang�, cocher la case "Filter pulses for change in current amplitude". Un nouveau Level Channel, portant le m�me nom que celui s�lectionn� dans la case "Pulse Event" sera alors cr��.
  --Le script permet de plotter la fr�quence moyenne, mesure sur un certain pourcentage de la dur�e du pulse (default, 75%) en partant de la fin du pulse pour ne pas mesurer la p�riode d'adaptation.
  --s'il l'on pr�f�re plotter un ISI pr�cis (par ex, 1er interval inter-spike), d�cocher la case "Plot stationary frequency" et choisir l'ISI d�sir� dans la boite "Plot ISI n�"
-Cliquer sur OK
-Le script affiche les pulses successivement, et demande de valider la zone de mesure.
-Une fois tous les pulses pass�s en revue (ou si la touche "Yes to all" a �t� press�e) la courbe IF est affich�e. Chaque point repr�sente un pulse.

* analysis_IFcurve_ramp.s2s
Ce script permet de plotter une courbe IF en r�ponse � une rampe de courant. Il mesure �galement:
  -les fr�quences de recrutement et de d�recrutement
  -le seuil en voltage du premier potentiel d'action
  -la pente de la courve IF
-Lancer le script sur un fichier de donn�es (.smr)
-Rentrer les informations n�cessaires dans la boite de dialogue qui s'affiche
-le script propose de sauvegarder la courbe IF g�n�r�e.
-les valeurs num�riques sont affich�es sous forme de curseurs dans le fichier de donn�es, et sont �crites dans le fichier Log.
-3 valeurs de gains sont mesur�es:
  --le gain ascendant ("ascSlope"), calcul� sur toute la dur�e de la branche ascendante
  --le gain descendant ("descSlope"), calcul� sur toute la dur�e de la branche descendante
  --le gain global ("Slope"), calcul� sur l'ensemble de la rampe

* analysis_IVcurve.s2s
Ce script plot la courbe IV en r�ponse � une rampe de courant en voltage clamp
Une fois la courbe brute plott�e, il estime le potentiel d'activation du PIC (point de pente nulle), et propose une r�gion sur laquelle faire l'estimation de la conductance de fuite. Celle-ci est alors soustraite pour obtenir la courbe "leak-substracted" sur laquelle est estim�e l'amplitude du PIC.
Appuyer sur "Accept" pour sauvegarder les fichiers de r�sultats. Le script �crira dans le Log les valeurs qu'il a estim� automatiquement que si l'utilisateur r�pond "Yes" � la question "Accept estimated values?". Dans la n�gative, seule les valeurs que l'utilisateur a mesur� lui-m�me en changeant la position des curseurs seront �crits dans le Log.

* analysis_spike.s2s
Ce script mesure diff�rents param�tres sur un spike g�n�r� par un pulse de courant d�polarisant bref. Il se lance sur un fichier moyenn� (.srf).
il mesure les param�tres suivants:
  -- RMP
  -- Spike height
  -- Spike half-width
  -- AHP Amplitude
  -- AHP Time-to-peak
  -- AHP Duration
  -- AHP 1/2 relaxation time
  -- AHP time constant
NB: pour aider le script � trouver le pic de l'AHP, en particulier lorsqu'il y a beaucoup de bruit, il est possible de zoomer sur l'AHP pour supprimer toute la r�gion en fin d'AHP o� le potentiel est revenu � la valeur de repos

* analysis_Accomodation.s2s
ce script mesure le seuil en voltage des potentiels d'action (voltage ou la vitesse d'�volution du potentiel d�passe 10mV/ms) et le plot sur un graphique en fonction du courant inject�.
Marche sur n'importe quel type de fichier de donn�e (.smr).

* analysis_ZAP.s2s
ce script mesure l'imp�dance d'un MN en r�ponse � un courant sinusoidal de fr�quence croissante (ZAP).
Le script se lance sur un fichier moyenn� (.srf) contenant au moins la moyenne du potentiel de membrane et du courant inject�. Pour avoir plusieurs channels moyenn�s en m�me temps, s�lectionner les channels d'int�r�t (Ctrl+Click) avant de lancer la proc�dure de moyennage. Dans la boite de dialogue de moyennage, dans la liste "Channels", s�lectionner "Selected:". Puis faire la moyenne comme d'habitude.
Le script plotte le module de l'imp�dance |Z|=FFT(Vm)/FFT(Im) entre les fr�quences choisies dans la boite de dialogue. Il peut �galement lisser le r�sultat, en calculant une moyenne flottante sur un nombre de points choisi dans la boite de dialogue. Dans ce cas, le script estime la valeur de la fr�quence de r�sonance et calcule la Qualit� de la r�sonance. Ces valeurs sont report�es dans le log. 