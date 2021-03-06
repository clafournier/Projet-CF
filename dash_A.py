import streamlit as st
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
from st_btn_select import st_btn_select
import numpy as np

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
start_date =  datetime.date(2000, 1, 1)
end_date =  datetime.date.today()

# Configuration de la page (Page setting)
st.set_page_config(layout="wide")

st.write('______') # ligne pour éviter le floue d'affichage du haut  
 
with open('style.css') as f:

    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown('<p class="font3"> Travail de session FIN30521 par Claude Fournier</p>', unsafe_allow_html=True) 

st.markdown(""" <style>

.font1 {font-size:35px ;
        font-family: 'Cooper Black';
        color: #FF9633;
        text-align: center;
        border: 3px solid green; }

 .font2 {font-size:25px ;
        font-family: 'Cooper Black';
        color: gold;
        text-align: center;
        border: 3px solid blue;  }

 .font3 {font-size:25px ;
        font-family: 'Cooper Black';
        color: lightskyblue;
        text-align: center;
        border: 3px solid black; }

</style> """,

unsafe_allow_html=True)   
 
# Éléments de la première rangée du dashboard (Row A)
a1, a2, a3, a4 = st.columns(4)

# Premier élément du tableau
with a1:
    st.image('./Tableau de bord.png')
   
# Deuxième élément du tableau
SP500 = yf.Ticker('^GSPC') # Obtenir le ticker data
SP500_DATA = SP500.history(period='5d')
r_sp500 = (SP500_DATA.Close[-1] - SP500_DATA.Close[-2])/SP500_DATA.Close[-2]
a2.metric("S&P 500", f"{SP500_DATA.Close[-1] :,.0f}", f"{100*r_sp500:.2f} %")



# Troisième élément du tableau
nasdaq = yf.Ticker('^IXIC') # Obtenir le ticker data
nasdaq_DATA = nasdaq.history(period='5d')
r_nasdaq = (nasdaq_DATA.Close[-1] - nasdaq_DATA.Close[-2])/nasdaq_DATA.Close[-2]
a3.metric("NASDAQ Composite", f"{nasdaq_DATA.Close[-1] :,.0f}", f"{100*r_nasdaq:.2f} %")

# Quatrième élément du tableau
SP_TSX = yf.Ticker('^GSPTSE') # Obtenir le ticker data
SP_TSX_DATA = SP_TSX.history(period='5d')
r_sp_tsx = (SP_TSX_DATA.Close[-1] - SP_TSX_DATA.Close[-2])/SP_TSX_DATA.Close[-2]
a4.metric("S&P/TSX", f"{SP_TSX_DATA.Close[-1] :,.0f}", f"{100*r_sp_tsx:.2f} %")

 
# Éléments de la deuxième rangée (Row B)
b1, b2, b3, b4 = st.columns(4)

# Block 1 : Premier élément """Cad/USD"""
cad_usd = yf.Ticker('CADUSD=X') # Get ticker data
cad_usd_DATA = cad_usd.history(period='5d')
r_cad_usd = (cad_usd_DATA.Close[-1] - cad_usd_DATA.Open[-1])/cad_usd_DATA.Open[-1]
b1.metric("CAD/USD", f"{cad_usd_DATA.Close[-1] :.3f}", f"{100*r_cad_usd :.2f} %")


# Block 1 : Deuxième élément """USD/EUR"""
usd_eur = yf.Ticker('EUR=X') # Obtenir le ticker data 
usd_eur_DATA = usd_eur.history(period='5d')
r_usd_eur = (usd_eur_DATA.Close[-1] - usd_eur_DATA.Open[-1])/usd_eur_DATA.Open[-1]
b1.metric("USD/EUR", f"{usd_eur_DATA.Close[-1] :.3f}", f"{100*r_usd_eur :.2f} %")

 # Block 2 : Premier élément """WTI"""
wti = yf.Ticker('CL=F') # Obtenir le ticker data
wti_DATA = wti.history(period='5d')
diff_wti = wti_DATA.Close[-1] - wti_DATA.Close[-2]
r_wti = diff_wti/wti_DATA.Close[-2]
b2.metric("Pétrole (WTI)", f"{wti_DATA.Close[-1] :.2f}", f"{diff_wti:.2} ({100*r_wti :.2f}%)")

# Block 2 : Deuxième élément """Natural Gas"""
natural_gas = yf.Ticker('NG=F') # Obtenir le ticker data 
natural_gas_DATA = natural_gas.history(period='5d')
diff_natural_gas = natural_gas_DATA.Close[-1] - natural_gas_DATA.Close[-2]
r_nga = diff_natural_gas/natural_gas_DATA.Close[-2]
b2.metric("Natural Gas (NGA)", f"{natural_gas_DATA.Close[-1] :.2f}", f"{diff_natural_gas:.2} ({100*r_nga :.2f}%)")

# Block 3 : Premier élément """Taux directeur USA 5 ans"""
us5y = yf.Ticker('^FVX') # Obtenir le ticker data
us5y_DATA = us5y.history(period='5d')
diff_us5y = us5y_DATA.Close[-1] - us5y_DATA.Close[-2]
r_us5y = diff_us5y/us5y_DATA.Close[-2]
b3.metric("Taux US   5 ans", f"{us5y_DATA.Close[-1] :.3f}", f"{diff_us5y:.2} ({100*r_us5y :.2f}%)")


# Block 3 : Deuxième élément """Taux directeur USA 10 ans"""" 
us10y = yf.Ticker('^TNX') # Obtenir le ticker data
us10y_DATA = us10y.history(period='5d')
diff_us10y = us10y_DATA.Close[-1] - us10y_DATA.Close[-2]
r_us10y = diff_us10y/us10y_DATA.Close[-2]
b3.metric("Taux US   10 ans", f"{us10y_DATA.Close[-1] :.3f}", f"{diff_us10y:.2} ({100*r_us10y :.2f}%)")


# Block  4 : Premir élément volatilité """VIX"""
volatilité = yf.Ticker('^VIX') # Obtenir les données du ticker 
volatilité_DATA = volatilité.history(period='5d')
diff_volatilité = volatilité_DATA.Close[-1] - volatilité_DATA.Close[-2]
r_volatilité = diff_volatilité/volatilité_DATA.Close[-2]
b4.metric("CBOE Volatility Index (VIX)", f"{volatilité_DATA.Close[-1] :.2f}", f"{diff_volatilité:.2} ({100*r_volatilité :.2f}%)")

# Block 4 : Deuxième élément """ACWI"""
volatilité = yf.Ticker('ACWI') # Obtenir les données du ticker 
volatilité_DATA = volatilité.history(period='5d')
diff_volatilité = volatilité_DATA.Close[-1] - volatilité_DATA.Close[-2]
r_volatilité = diff_volatilité/volatilité_DATA.Close[-3]
b4.metric("Ishare MSCI ACWI ETF", f"{volatilité_DATA.Close[-1] :.2f}", f"{diff_volatilité:.2} ({100*r_volatilité :.2f}%)")

# Éléments de la troième rangé """ Precious Metals Stocks (row 3)
s1, s2, s3, s4 = st.columns(4)

# Block 1 :  """Gold"""
Or = yf.Ticker('GC=F') # Obtenir les données du ticker
Or_DATA = Or.history(period='5d')
diff_Or = Or_DATA.Close[-1] - Or_DATA.Close[-2]
r_Or = diff_Or/Or_DATA.Close[-2]
s1.metric("Or", f"{Or_DATA.Close[-1] :.2f}", f"{diff_Or:.2} ({100*r_Or :.2f}%)")


# Block 2 :  """Silver"""
Silver = yf.Ticker('SI=F') # Obtenir les données du ticker
Silver_DATA = Silver.history(period='5d')
diff_Silver = Silver_DATA.Close[-1] - Silver_DATA.Close[-2]
r_Silver = diff_Silver/Silver_DATA.Close[-2]
s2.metric("Silver", f"{Silver_DATA.Close[-1] :.2f}", f"{diff_Silver:.2} ({100*r_Silver :.2f}%)")

# Block 3 : """Copper"""
copper = yf.Ticker('HG=F') # Obtenir les données du ticker
copper_DATA = copper.history(period='5d')
diff_copper = copper_DATA.Close[-1] - copper_DATA.Close[-2]
r_copper = diff_copper/copper_DATA.Close[-2]
s3.metric("Copper", f"{copper_DATA.Close[-1] :.2f}", f"{diff_copper:.2} ({100*r_copper :.2f}%)")

# Block 4 """ Platinum"""
Platinum = yf.Ticker('SI=F') # Obtenir les données du ticker
Platinum_DATA = Platinum.history(period='5d')
diff_Platinum = Platinum_DATA.Close[-1] - Platinum_DATA.Close[-2]
r_Platinum = diff_Platinum/Platinum_DATA.Close[-2]
s4.metric("Platinum", f"{Platinum_DATA.Close[-1] :.2f}", f"{diff_Platinum:.2} ({100*r_Platinum:.2f}%)")

st.write('______')

# """Nouvelle section du tableau"""

# Inscription de la date et heure du rapport dashboard
date = st.sidebar.date_input('Données en date du :', datetime.date.today())


heure = datetime.datetime.now()
#heure_actuelle = heure.strftime("%H:%M:%S")
st.sidebar.time_input('Heure des informations actuelles :', heure)


# Récupération des données (tickers data) (Création d'un portefeuille - Liste no 1)

ticker_list1 = ['AMZN', 'MSFT', 'WMT','SHOP.TO', 'TD.TO', 'SAP.TO' ]
tickerSymbol1 = st.sidebar.selectbox('Portefeuille # 1 : Choisir une entreprise :', ticker_list1) # Sélection ticker symbol
tickerData1 = yf.Ticker(tickerSymbol1) # # Obtenir les données du ticker
tickerDf1 = tickerData1.history(period='max') # Obtenir l'hitorique des cours pour ce ticker
entreprise1 = tickerData1.info["shortName"]

# Récupération des données (tickers data) (Création d'un portefeuille-Liste no 2)

ticker_list2 = ['INE.TO', 'BLX.TO','DOL.TO','CAS.TO','SU']
tickerSymbol2 = st.sidebar.selectbox('Portefeuille # 2 : Choisir une entreprise :', ticker_list2) # Sélection du ticker symbol
tickerData2 = yf.Ticker(tickerSymbol2) # Obtenir les données du ticker 
tickerDf2 = tickerData2.history(period='1d', start=start_date, end=end_date) # Obtenir l'hitorique des cours pour ce ticker
entreprise2 = tickerData2.info["shortName"]

# Récupération des données (tickers data) (Création d'un portefeuille-Liste no 3)

ticker_list3 = ['PYPL','TWTR','RFP.TO','TSLA']
tickerSymbol3 = st.sidebar.selectbox('Portefeuille # 3 : Choisir une entreprise :', ticker_list3) # Sélection du ticker symbol
tickerData3 = yf.Ticker(tickerSymbol3) # Obtenir les données du ticker 
tickerDf3 = tickerData3.history(period='1d', start=start_date, end=end_date) # Obtenir l'hitorique des cours pour ce ticker
entreprise3 = tickerData3.info["shortName"]

# Récupération des données (tickers data) (Création d'un porte feuille-Liste no 4)

ticker_list4 = ['MRU.TO', 'ATD.TO','RFP.TO']
tickerSymbol4 = st.sidebar.selectbox('Portefeuille # 4 : Choisir une entreprise :', ticker_list4) # Selection du ticker symbol
tickerData4 = yf.Ticker(tickerSymbol4) # Get ticker data
tickerDf4 = tickerData4.history(period='1d', start=start_date, end=end_date) # Obtenir l'hitorique des cours pour ce ticker
entreprise4 = tickerData4.info["shortName"]

# Nouveau block

st.write(f" ### Cours de l'action de l'entreprise : {entreprise1.title()}")
st.markdown('#####')

# Cours de l'entreprise illustré sur un choix de différentes périodes
selection = st_btn_select(('5 jours', '1 mois', '6 mois', '1 an', '3 ans', '5 ans', '10 ans'))
st.write(f" ### Tableau comparatif avec les entreprises :\n ##### - {entreprise2.title()} \n ##### - {entreprise3.title()} \n ##### - {entreprise4.title()}")

# Figure pour illustrer 4 axes
fig1, ax = plt.subplots(2,2,figsize = (24, 16), dpi = 400,facecolor ='#F5F5DC')


ax1 = ax[0,0] # Localisation graphique 1
ax2 = ax[0,1] # Localisation graphique 2
ax3 = ax[1,0] # Localisation graphique 3
ax4 = ax[1,1] # Localisation graphique 4

# Configuration et attributs du premier graphique illustré
ax1.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large',) # Information de l'axe des x (Label)
ax1.set_ylabel ("Cours du Titre", color ='k',fontsize='xx-large')    # Information de l'axe des y (Label)
ax1.set_title (tickerSymbol1,fontsize='xx-large',color ='blue')      # Titre du graphique illustré ( Ticker symbol) )
ax1.legend (facecolor='k', labelcolor='w')                           # Attributs de la légende
ax1.grid(color='grey', linestyle='--', linewidth=0.5)

# Configuration et attributs du deuxième graphique illustré          # Idem ax1
ax2.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax2.set_ylabel ("Cours du Titre", color ='k',fontsize='xx-large')
ax2.set_title (tickerSymbol2,fontsize='xx-large',color ='blue')
ax2.legend (facecolor='k', labelcolor='w')
ax2.grid(color='grey', linestyle='--', linewidth=0.5)

# Configuration et attributs du troisième graphique illustré        # Idem ax1
ax3.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax3.set_ylabel ("Cours du Titre", color ='k',fontsize='xx-large')
ax3.set_title (tickerSymbol3,fontsize='xx-large',color ='blue')
ax3.legend (facecolor='k', labelcolor='w', fontsize='larger')
ax3.grid(color='grey', linestyle='--', linewidth=0.5)

# Configuration et attributs du quatrième graphique illustré        # Idem ax1
ax4.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax4.set_ylabel ("Cours du Titre", color ='k',fontsize='xx-large')
ax4.set_title (tickerSymbol4,fontsize='xx-large',color ='blue')
ax4.legend (facecolor='k', labelcolor='w')
ax4.grid(color='grey', linestyle='--', linewidth=0.5)


# Section de la sélection de la période à afficher des graphiques
# Fonctions pour déterminer le choix de la période affichée
if selection == '5 jours':                                                # sélection 5 jours
    ax1.plot(tickerDf1.Close[-5:-1], color = 'red',  label = selection)
    ax2.plot(tickerDf2.Close[-5:-1], color = 'green',label = selection)
    ax3.plot(tickerDf3.Close[-5:-1], color = 'cyan', label = selection) 
    ax4.plot(tickerDf4.Close[-5:-1], color = 'blue', label = selection)
    
elif selection == '1 mois':                                               # sélection 1 mois
    ax1.plot(tickerDf1.Close[-30:-1], color = 'blue', label = selection)  
    ax2.plot(tickerDf2.Close[-30:-1], color = 'blue', label = selection)
    ax3.plot(tickerDf3.Close[-30:-1], color = 'green',label = selection)
    ax4.plot(tickerDf4.Close[-30:-1], color = 'black',label = selection)

elif selection == '6 mois':                                                # sélection 6 mois
    ax1.plot(tickerDf1.Close[-180:-1], color = 'green', label = selection) 
    ax2.plot(tickerDf2.Close[-180:-1], color = 'black', label = selection)
    ax3.plot(tickerDf3.Close[-180:-1], color = 'red',   label = selection)
    ax4.plot(tickerDf4.Close[-180:-1], color = 'blue',  label = selection)


elif selection == '1 an':                                                   # sélection 1 an
    ax1.plot(tickerDf1.Close[-252:-1], color = 'cyan',  label = selection)
    ax2.plot(tickerDf2.Close[-252:-1], color = 'black', label = selection)
    ax3.plot(tickerDf3.Close[-252:-1], color = 'blue',  label = selection)
    ax4.plot(tickerDf4.Close[-252:-1], color = 'red',   label = selection)


elif selection == '3 ans':                                                   # sélection 3 ans
    ax1.plot(tickerDf1.Close[-3*252:-1], color = 'red',  label = selection)
    ax2.plot(tickerDf2.Close[-3*252:-1], color = 'cyan', label = selection)
    ax3.plot(tickerDf3.Close[-3*252:-1], color = 'black',label = selection)
    ax4.plot(tickerDf4.Close[-3*252:-1], color = 'blue', label = selection)

elif selection == '5 ans':                                                   # sélection 5 ans
    ax1.plot(tickerDf1.Close[-5*252:-1], color = 'cyan', label = selection)
    ax2.plot(tickerDf2.Close[-5*252:-1], color = 'red',  label = selection)
    ax3.plot(tickerDf3.Close[-5*252:-1], color = 'black',label = selection)
    ax4.plot(tickerDf4.Close[-5*252:-1], color = 'blue', label = selection)


elif selection == '10 ans':
    ax1.plot(tickerDf1.Close[-10*252:-1], color = 'green',  label = selection)
    ax2.plot(tickerDf2.Close[-10*252:-1], color = 'cyan',   label = selection)
    ax3.plot(tickerDf3.Close[-10*252:-1], color = '#0000ff',label = selection)
    ax4.plot(tickerDf4.Close[-10*252:-1], color = 'red',    label = selection)


# Afficher la légende
ax1.legend (facecolor='k', labelcolor='w') 
ax2.legend (facecolor='k', labelcolor='w')
ax3.legend (facecolor='k', labelcolor='w')
ax4.legend (facecolor='k', labelcolor='w')

st.write("_______")


 # Ici on va dessiner les courbes et autres attributs sur la figure des 4 graphiques affichés (axes)  

fig1.autofmt_xdate(rotation=45 ) # ici les dates sur les axes s'ajustent d'une facon automatique

st.pyplot(fig1)

st.write("_______")

# Nouvelle section dans le dashbord concernant l'enteprise concernée
st.write(f"### Information financière de l'entreprise : {entreprise1.title()}")

c1, c2, c3, c4, c5 = st.columns(5) # création de 5 block dans la rangée

diff_tickerDf1 = tickerDf1.Close[-1] - tickerDf1.Close[-2]
r_tickerDf1 = diff_tickerDf1/tickerDf1.Close[-2]
c1.metric(f"{tickerSymbol1}", f"{tickerDf1.Close[-1] :.2f} $", f"{diff_tickerDf1:.2f} ({100*r_tickerDf1 :.2f}%)")

sector= tickerData1.info["sector"] # Ici on indique le secteur de l'entreprise
c1.metric('Secteur', sector)

Day_High = tickerData1.info ["dayHigh"]
Day_Low  = tickerData1.info ["dayLow"]
c2.metric ("Day High", f"{Day_High:.2f} $")
c2.metric ("Day Low", f"{Day_Low:.2f} $")

recommandation1 = tickerData1.info["recommendationKey"]  # Ici on indique la recommandation des analystes
c3.metric("Recommandation", recommandation1.title())

Prix_cible = tickerData1.info["targetMeanPrice"]         # Ici on va chercher le cours cible
c3.metric("Prix cible ", f'{Prix_cible:.2f} $')

Beta = tickerData1.info["beta"]                          # Ici on va chercher le beta de l'entreprise
c4.metric("beta ", round(Beta,2))

CB1 = tickerData1.info["forwardPE"]                      # Ici on va chercher le ratio cours bénéfice
c4.metric("C/B",  f'{CB1:.2f}' )

marge = tickerData1.info["profitMargins"]                # Ici on va chercher le Pourcentage de la marge brute
c5.metric("Marge brute ", f"{round(marge*100, 2)}%" )

ROA = tickerData1.info["returnOnAssets"]                 # Ici on va chercher le pourcentage du "Return Of Asset"
c5.metric("ROA ", f"{round(ROA*100, 2)}%" )


st.write('______')

# Nouvelle section
# Description et information à propos de l'entreprise

string_logo = '<img src=%s>' % tickerData1.info['logo_url'] # Ici on affiche le logo de l'entreprise principale

st.markdown(string_logo, unsafe_allow_html=True) 

st.write(" ##### Description sommaire de l'entreprise")
tickerData1.info["longBusinessSummary"]                    # Ici on affiche un sommaire (description) de l'entreprise

st.write("_______")

# Block
# Description des détenteurs principaux de l'actionnariats

st.write(" ##### Détenteurs institutionnels majeurs :")

tickerData1.institutional_holders # Ici les principaux détenteurs de l'actionnariat de l'enteprise
st.write("_______")

st.write(" ##### Site Web :",tickerData1.info ["website"])


st.write("_______")

# (Optionel) pour autres informations général sur Yahoo finance employer  tickerData1.info 
# tickerData1.info


# Notes personnelles pour moi vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #
# """Autre chose à voir et à concrétiser si possibilité plus tard ??""""

# fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']],constrained_layout=True)

# for label, ax in axs.items():
    # label physical distance in and down:
    # trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    # ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
           #  fontsize='medium', verticalalignment='top', fontfamily='serif',
            # bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
# plt.show()   
