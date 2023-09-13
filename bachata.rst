Bachata
=======

.. comp:: Basic 1
   :id: C_BASIC_1
   :status: open
   :tags: user;login
   :collapse: false

   Der Basic-Schritt besteht aus 8 Schlägen. 
   Auf 1 für den Herr nach links. 
   Schritt, schritt, schritt, tap. 

.. comp:: Basic 2
   :id: C_BASIC_2
   :status: open
   :tags: user;login
   :collapse: false

   Der Basic-Schritt besteht aus 8 Schlägen. 
   Auf 5 nach rechts. 
   Schritt, Schritt, Schritt, tipp.

.. int:: Basic 1
   :id: I_BASIC_1
   :status: open
   :has_direction: C_BASIC_1
   :follows_after: I_Damendrehung_links_1
   :tags: user;login
   :collapse: false

   Schritt 1 bis 4 vom Basic-Schritt.

.. int:: Basic 2
   :id: I_BASIC_2
   :status: open
   :has_direction: C_BASIC_2
   :follows_after: I_BASIC_1, I_Koerbchen_2
   :tags: user;login
   :collapse: false

   Schritt 5 bis 8 vom Basic-Schritt.

.. int:: Damendrehung links einhändig
   :id: I_Damendrehung_links_1
   :status: open
   :has_direction: C_BASIC_2
   :follows_after: I_BASIC_1
   :requires_preperation: P_linke_Hand_heben
   :tags: user;login
   :collapse: false

   Schritt 5 bis 8 vom Basic-Schritt. Dame dreht dabei nach links.

.. int:: Körbchen
   :id: I_Koerbchen_1
   :status: open
   :has_direction: C_BASIC_2
   :follows_after: I_BASIC_1
   :requires_preperation: P_linke_Hand_heben
   :tags: user;login
   :collapse: false

   Linke Hand führt Linksdrehung. Rechte Hand wird auf Hüfthöhe geführt. Dame endet im 90 grad Winkel zum Herr.

.. int:: Körbchen zurück
   :id: I_Koerbchen_2
   :status: open
   :has_direction: C_BASIC_1
   :follows_after: I_Koerbchen_1
   :tags: user;login
   :collapse: false

   Schubs mit dem rechten Arm und linke Hand schräg nach links vorne anheben.

.. prep:: Linke Hand heben
   :id: P_linke_Hand_heben
   :status: open
   :tags: user;login
   :collapse: false

   Linke Hand auf den letzten Schlag anheben. 

