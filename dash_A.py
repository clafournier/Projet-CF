import streamlit as st
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
from st_btn_select import st_btn_select
import numpy as np

# """"""""""""""""""""""""""""""""""""""""""
start_date =  datetime.date(2000, 1, 1)
end_date =  datetime.date.today()

# Page setting

st.set_page_config(layout="wide")
 
with open('style.css') as f:

    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

 
# Éléments de la première rangée (Row A)

a1, a2, a3, a4 = st.columns(4)

with a1:

    st.image('./Tableau de bord.png')
   


SP500 = yf.Ticker('^GSPC') # Obtenir le ticker data

SP500_DATA = SP500.history(period='1d', interval = "1m")

SP500_DATA2 = SP500.history(period='5d')

r_sp500 = (SP500_DATA2.Close[-1] - SP500_DATA2.Close[-2])/SP500_DATA2.Close[-2]

a2.metric("S&P 500", f"{SP500_DATA.Close[-1] :,.0f}", f"{100*r_sp500:.2f} %")


nasdaq = yf.Ticker('^IXIC') # Obtenir le ticker data

nasdaq_DATA = nasdaq.history(period='5d', interval = "1m")

nasdaq_DATA2 = nasdaq.history(period='5d', start=start_date, end=end_date)

r_nasdaq = (nasdaq_DATA2.Close[-1] - nasdaq_DATA2.Close[-2])/nasdaq_DATA2.Close[-2]

a3.metric("NASDAQ Composite", f"{nasdaq_DATA.Close[-1] :,.0f}", f"{100*r_nasdaq:.2f} %")


SP_TSX = yf.Ticker('^GSPTSE') # Obtenir le ticker data

SP_TSX_DATA = SP_TSX.history(period='5d', interval = "1m")

SP_TSX_DATA2 = SP_TSX.history(period='5d', start=start_date, end=end_date)

r_sp_tsx = (SP_TSX_DATA2.Close[-1] - SP_TSX_DATA2.Close[-2])/SP_TSX_DATA2.Close[-2]

a4.metric("S&P/TSX", f"{SP_TSX_DATA.Close[-1] :,.0f}", f"{100*r_sp_tsx:.2f} %")

 
# Éléments de la deuxième rangée (Row B)
# """Cad/USD"""

b1, b2, b3, b4 = st.columns(4)

cad_usd = yf.Ticker('CADUSD=X') # Get ticker data

cad_usd_DATA = cad_usd.history(period='5d', interval = "1m")

cad_usd_DATA2 = cad_usd.history(period='5d', start=start_date, end=end_date)

r_cad_usd = (cad_usd_DATA2.Close[-1] - cad_usd_DATA2.Close[-2])/cad_usd_DATA2.Close[-2]

b1.metric("CAD/USD", f"{cad_usd_DATA.Close[-1] :.3f}", f"{100*r_cad_usd :.2f} %")

# """USD/EUR"""
usd_eur = yf.Ticker('EUR=X') # Obtenir le ticker data (Ajouter par Claude)

usd_eur_DATA = usd_eur.history(period='5d', interval = "1m")

usd_eur_DATA2 = usd_eur.history(period='5d', start=start_date, end=end_date)

r_usd_eur = (usd_eur_DATA2.Close[-1] - usd_eur_DATA2.Close[-2])/usd_eur_DATA2.Close[-2]

b1.metric("USD/EUR", f"{usd_eur_DATA.Close[-1] :.3f}", f"{100*r_usd_eur :.2f} %")

 # """WTI"""
wti = yf.Ticker('CL=F') # Obtenir le ticker data

wti_DATA = wti.history(period='5d', interval = "1m")

wti_DATA2 = wti.history(period='5d', start=start_date, end=end_date)

diff_wti = wti_DATA2.Close[-1] - wti_DATA2.Close[-2]

r_wti = diff_wti/wti_DATA2.Close[-2]

b2.metric("Pétrole (WTI)", f"{wti_DATA.Close[-1] :.2f}", f"{diff_wti:.2} ({100*r_wti :.2f}%)")

# """Natural Gas"""
natural_gas = yf.Ticker('NG=F') # Obtenir le ticker data (ajouter par Claude)

natural_gas_DATA = natural_gas.history(period='5d', interval = "1m")

natural_gas_DATA2 = natural_gas.history(period='5d', start=start_date, end=end_date)

diff_natural_gas = natural_gas_DATA2.Close[-1] - natural_gas_DATA2.Close[-2]

r_nga = diff_natural_gas/natural_gas_DATA2.Close[-2]

b2.metric("Natural Gas (NGA)", f"{natural_gas_DATA.Close[-1] :.2f}", f"{diff_natural_gas:.2} ({100*r_nga :.2f}%)")

# """Bonds"""
us5y = yf.Ticker('^FVX') # Get ticker data

us5y_DATA = us5y.history(period='1d', start=start_date, end=end_date)

diff_us5y = us5y_DATA.Close[-1] - us5y_DATA.Close[-2]

r_us5y = diff_us5y/us5y_DATA.Close[-2]

b3.metric("Taux US   5 ans", f"{us5y_DATA.Close[-1] :.3f}", f"{diff_us5y:.2} ({100*r_us5y :.2f}%)")


# """Taux directeur USA"""" 
us10y = yf.Ticker('^TNX') # Get ticker data

us10y_DATA = us10y.history(period='1d', start=start_date, end=end_date)

diff_us10y = us10y_DATA.Close[-1] - us10y_DATA.Close[-2]

r_us10y = diff_us10y/us10y_DATA.Close[-2]

b3.metric("Taux US   10 ans", f"{us10y_DATA.Close[-1] :.3f}", f"{diff_us10y:.2} ({100*r_us10y :.2f}%)")

 

# """VIX"""
volatilité = yf.Ticker('^VIX') # Obtenir les données du ticker 

volatilité_DATA = volatilité.history(period='5d', interval = "1m")

volatilité_DATA2 = volatilité.history(period='1d', start=start_date, end=end_date)

diff_volatilité = volatilité_DATA2.Close[-1] - volatilité_DATA2.Close[-2]

r_volatilité = diff_volatilité/volatilité_DATA2.Close[-2]

b4.metric("Volatilité (VIX)", f"{volatilité_DATA.Close[-1] :.2f}", f"{diff_volatilité:.2} ({100*r_volatilité :.2f}%)")

# """VIX"""
volatilité = yf.Ticker('^VIX') # Obtenir les données du ticker 

volatilité_DATA = volatilité.history(period='5d', interval = "1m")

volatilité_DATA2 = volatilité.history(period='1d', start=start_date, end=end_date)

diff_volatilité = volatilité_DATA2.Close[-1] - volatilité_DATA2.Close[-2]

r_volatilité = diff_volatilité/volatilité_DATA2.Close[-2]

b4.metric("Volatilité (VIX)", f"{volatilité_DATA.Close[-1] :.2f}", f"{diff_volatilité:.2} ({100*r_volatilité :.2f}%)")

# Éléments de la troième rangé """ Precious Metals Stocks (row 3)

# """Gold"""
s1, s2, s3, s4 = st.columns(4)

Or = yf.Ticker('GC=F') # Obtenir les données du ticker

Or_DATA = Or.history(period='5d', interval = "1m")

Or_DATA2 = Or.history(period='1d', start=start_date, end=end_date)

diff_Or = Or_DATA2.Close[-1] - Or_DATA2.Close[-2]

r_Or = diff_Or/Or_DATA2.Close[-2]

s1.metric("Or", f"{Or_DATA.Close[-1] :.2f}", f"{diff_Or:.2} ({100*r_Or :.2f}%)")


# """Silver"""
Silver = yf.Ticker('SI=F') # Obtenir les données du ticker

Silver_DATA = Silver.history(period='5d', interval = "1m")

Silver_DATA2 = Silver.history(period='1d', start=start_date, end=end_date)

diff_Silver = Silver_DATA2.Close[-1] - Silver_DATA2.Close[-2]

r_Silver = diff_Silver/Silver_DATA2.Close[-2]

s2.metric("Silver", f"{Silver_DATA.Close[-1] :.2f}", f"{diff_Silver:.2} ({100*r_Silver :.2f}%)")

# """Copper"""
copper = yf.Ticker('HG=F') # Obtenir les données du ticker

copper_DATA = copper.history(period='5d', interval = "1m")

copper_DATA2 = copper.history(period='1d', start=start_date, end=end_date)

diff_copper = copper_DATA2.Close[-1] - copper_DATA2.Close[-2]

r_copper = diff_copper/copper_DATA2.Close[-2]

s3.metric("Copper", f"{copper_DATA.Close[-1] :.2f}", f"{diff_copper:.2} ({100*r_copper :.2f}%)")

# """ Platinum"""
Platinum = yf.Ticker('SI=F') # Obtenir les données du ticker

Platinum_DATA = Platinum.history(period='5d', interval = "1m")

Platinum_DATA2 = Platinum.history(period='1d', start=start_date, end=end_date)

diff_Platinum = Platinum_DATA2.Close[-1] - Platinum_DATA2.Close[-2]

r_Platinum = diff_Platinum/Platinum_DATA2.Close[-2]

s4.metric("Platinum", f"{Platinum_DATA.Close[-1] :.2f}", f"{diff_Platinum:.2} ({100*r_Platinum:.2f}%)")

st.write('______')

# """Nouvelle section block"""

# Inscription de la date du rapport

date = st.sidebar.date_input('Données en date du :', datetime.date.today())
time = st.sidebar.time_input('Heure :', datetime.time())

st.write(date,textcolor = 'red')  # ici la couleur n'a rien changer ??
st.write (time)

# Récupération des données (tickers data) (Création d'un autre porte feuille - Liste no 1)

ticker_list1 = ['AMZN', 'MSFT', 'WMT','SHOP.TO', 'TD.TO', 'SAP.TO' ]
tickerSymbol1 = st.sidebar.selectbox('Porte feuille # 1 : Choisir une entreprise :', ticker_list1) # Select ticker symbol
tickerData1 = yf.Ticker(tickerSymbol1) # Get ticker data
tickerDf1 = tickerData1.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
entreprise1 = tickerData1.info["shortName"]

# Récupération des données (tickers data) (Création d'un autre porte feuille-Liste no 2)

ticker_list2 = ['INE.TO', 'BLX.TO','DOL.TO']
tickerSymbol2 = st.sidebar.selectbox('Porte feuille # 2 : Choisir une entreprise :', ticker_list2) # Sélection du ticker symbol
tickerData2 = yf.Ticker(tickerSymbol2) # Obtenir les données du ticker 
tickerDf2 = tickerData2.history(period='1d', start=start_date, end=end_date) # Obtenir les prix historiques pour ce ticker
entreprise2 = tickerData2.info["shortName"]

# Récupération des données (tickers data) (Création d'un autre porte feuille-Liste no 3)

ticker_list3 = ['FTS.TO', 'SU']
tickerSymbol3 = st.sidebar.selectbox('Porte feuille # 3 : Choisir une entreprise :', ticker_list3) # Sélection du ticker symbol
tickerData3 = yf.Ticker(tickerSymbol3) # Obtenir les données du ticker 
tickerDf3 = tickerData3.history(period='1d', start=start_date, end=end_date) # Obtenir les prix historiques pour ce ticker
entreprise3 = tickerData3.info["shortName"]

# Récupération des données (tickers data) (Création d'un autre porte feuille-Liste no 4)

ticker_list4 = ['MRU.TO', 'ATD.TO']
tickerSymbol4 = st.sidebar.selectbox('Porte feuille # 4 : Choisir une entreprise :', ticker_list4) # Select ticker symbol
tickerData4 = yf.Ticker(tickerSymbol4) # Get ticker data
tickerDf4 = tickerData4.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
entreprise4 = tickerData4.info["shortName"]

# Nouveau block
# Cours de l'entreprise illustré sur un choix de différentes périodes

st.write(f" ### Cours de l'action de l'entreprise : {entreprise1.title()}")

st.markdown('#####')

selection = st_btn_select(('5 jours', '1 mois', '6 mois', '1 an', '3 ans', '5 ans', '10 ans'))

st.write(f" ### Tableau comparatif avec les entreprises :\n ##### - {entreprise2.title()} \n ##### - {entreprise3.title()}, \n ##### - {entreprise4.title()}")

fig1, ax = plt.subplots(2,2,figsize = (24, 16), dpi = 400,facecolor ='grey')


plt.close('all')                          # espacement ok
plt.tight_layout(pad=1,w_pad=2, h_pad=2)  # ici je ne comprend pas, les arguments ne change rien ??
plt.rcdefaults()                          
plt.grid(color ='black')                                # grid ok
plt.legend ()                             # J'ai pas de légende 

ax1 = ax[0,0] # graphique 1
ax2 = ax[0,1] # graphique 2
ax3 = ax[1,0] # graphique 3
ax4 = ax[1,1] # graphique 4

ax1.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large',)
ax1.set_ylabel ("Cours de l'action", color ='w',fontsize='xx-large')
ax1.set_title (tickerSymbol1,fontsize='xx-large',color ='blue')
ax1.legend (facecolor='k', labelcolor='w')
    # ax1.plot('date', 'adj_close', data = tickerDf1[:300],color ="green")  # ???????
    # ax1 = np.linspace (start_date =  datetime.date(2000, 1, 1), end_date =  datetime.date.today())
    # ax1.plot ( ax1 )



ax2.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax2.set_ylabel ("Cours de l'action", color ='w',fontsize='xx-large')
ax2.set_title (tickerSymbol2,fontsize='xx-large',color ='blue')
ax2.legend (facecolor='k', labelcolor='w')
ax2.plot (start_date =  datetime.date(2000, 1, 1), end_date =  datetime.date.today(),color ='green') # ????? ne change rien

ax3.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax3.set_ylabel ("Cours de l'action", color ='w',fontsize='xx-large')
ax3.set_title (tickerSymbol3,fontsize='xx-large',color ='blue')
ax3.legend (facecolor='k', labelcolor='w')

ax4.set_xlabel ('Périodes (Times)', color ='k',fontsize='xx-large')
ax4.set_ylabel ("Cours de l'action", color ='w',fontsize='xx-large')
ax4.set_title (tickerSymbol4,fontsize='xx-large',color ='blue')
ax4.legend (facecolor='k', labelcolor='w')

# Section de la sélection de la période à afficher des graphiques

if selection == '5 jours':

    ax1.plot(tickerDf1.Close[-5:-1], color = 'red')


elif selection == '1 mois':

    ax1.plot(tickerDf1.Close[-30:-1],color ='blue')  

elif selection == '6 mois':

    ax1.plot(tickerDf1.Close[-180:-1],color = 'green')

elif selection == '1 an':

    ax1.plot(tickerDf1.Close[-22:-1], color ='cyan')

elif selection == '3 ans':

    ax1.plot(tickerDf1.Close[-3*252:-1])

elif selection == '5 ans':

    ax1.plot(tickerDf1.Close[-5*252:-1])

elif selection == '10 ans':

    ax1.plot(tickerDf1.Close[-10*252:-1], color = 'green')


st.write("_______")

# Block de choix # 2 de période à afficher
if selection == '5 jours':
    
    ax2.plot(tickerDf2.Close[-5:-1], color ='green') 

elif selection == '1 mois':

    ax2.plot(tickerDf2.Close[-30:-1], color = 'blue')  

elif selection == '6 mois':

    ax2.plot(tickerDf2.Close[-180:-1], color ='black')

elif selection == '1 an':

    ax2.plot(tickerDf2.Close[-22:-1],color ='black')

elif selection == '3 ans':

    ax2.plot(tickerDf2.Close[-3*252:-1])

elif selection == '5 ans':

    ax2.plot(tickerDf2.Close[-5*252:-1], color = 'red')

elif selection == '10 ans':

    ax2.plot(tickerDf2.Close[-10*252:-1], color ='cyan')


# Block de choix # 3 de période à afficher
if selection == '5 jours':
    
    ax3.plot(tickerDf3.Close[-5:-1], color = 'cyan') 

elif selection == '1 mois':

    ax3.plot(tickerDf3.Close[-30:-1], color ='green')  

elif selection == '6 mois':

    ax3.plot(tickerDf3.Close[-180:-1], color ='red')

elif selection == '1 an':

    ax3.plot(tickerDf3.Close[-22:-1], color ='black')

elif selection == '3 ans':

    ax3.plot(tickerDf3.Close[-3*252:-1])

elif selection == '5 ans':

    ax3.plot(tickerDf3.Close[-5*252:-1])

elif selection == '10 ans':

    ax3.plot(tickerDf3.Close[-10*252:-1],color = '#0000ff')

# Block de choix # 4 de période à afficher

if selection == '5 jours':
    
    ax4.plot(tickerDf4.Close[-5:-1]) 

elif selection == '1 mois':

    ax4.plot(tickerDf4.Close[-30:-1])  

elif selection == '6 mois':

    ax4.plot(tickerDf4.Close[-180:-1])

elif selection == '1 an':

    ax4.plot(tickerDf4.Close[-22:-1])

elif selection == '3 ans':

    ax4.plot(tickerDf4.Close[-3*252:-1])

elif selection == '5 ans':

    ax4.plot(tickerDf4.Close[-5*252:-1])

elif selection == '10 ans':

    ax4.plot(tickerDf4.Close[-10*252:-1])

 # Ici on va dessiner les courbes et autres attributs sur la figure des 4 graphiques affichés (axes)  

fig1.autofmt_xdate(rotation=45 ) # ici impossible d'appliquer une couleur ?? txtcolor = '#0000ff'

st.pyplot(fig1)

st.write("_______")

# nouvelle section dans le dashbord concernant l'enteprise concernée

st.write(f"### Information financière de l'entreprise : {entreprise1.title()}")

c1, c2, c3, c4 = st.columns(4)

diff_tickerDf1 = tickerDf1.Close[-1] - tickerDf1.Close[-2]
r_tickerDf1 = diff_tickerDf1/tickerDf1.Close[-2]

c1.metric(f"{tickerSymbol1}", f"{tickerDf1.Close[-1] :.2f}", f"{diff_tickerDf1:.3} ({100*r_tickerDf1 :.2f}%)")

sector= tickerData1.info["sector"]
c1.metric("Secteur", sector)

recommandation1 = tickerData1.info["recommendationKey"] 
c2.metric("Recommandation ", recommandation1.title())

Prix_cible = tickerData1.info["targetMeanPrice"]
c2.metric("Prix cible ", f'{Prix_cible:.2f}')

Beta = tickerData1.info["beta"]
c3.metric("beta ", round(Beta,2))

CB1 = tickerData1.info["forwardPE"]
c3.metric("C/B",  f'{CB1:.2f}' )

marge = tickerData1.info["profitMargins"]
c4.metric("Marge brute ", round(marge*100, 2),'%' )

ROA = tickerData1.info["returnOnAssets"]
c4.metric("ROA ", round(ROA*100, 2),'%' )

st.write('______')

# Block
# Description et information à propos de l'entreprise

string_logo = '<img src=%s>' % tickerData1.info['logo_url']

st.markdown(string_logo, unsafe_allow_html=True)

tickerData1.info["longBusinessSummary"] 

st.write("_______")

# Block
# Description des détenteurs de l'actionnariats

st.write(" ### Détenteurs institutionnels majeurs :")

tickerData1.institutional_holders

tickerData1.info


st.write("_______")


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #
# """Autre chose à voir et à concrétiser si possibilité plus tard ??""""

fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']],constrained_layout=True)

for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
plt.show()   

# """"nouveaux modules à être installés et importés par moi"""" To see later how to work ?

# import bond_pricing as bp

# import investpy as inv

# import matplotlib.transforms as mtransforms


x1 = np.linspace (start_date =  datetime.date(2000, 1, 1), end_date =  datetime.date.today())
ax1.plot ( x1 )

target2 = tickerData2.info["targetMeanPrice"]
diff_tickerData2 = tickerData2.Close[-1] - tickerData2.Close[-2]
r_tickerData2 = diff_tickerData2/tickerData2.Close[-2]
c2.metric("Prix cible ", target2.title())
c2.metric(f"{tickerData2.Close[-1] :.2f}", f"{diff_tickerData2:.2} ({100*r_tickerData2:.2f}%)")

fig, ax = plt.subplots()
ax.plot('date', 'adj_close', 
         data = data[:300],
         color ="green")
    
ax.xaxis.set_major_locator(years) 
ax.format_ydata = lambda x: '$% 1.2f' % x
ax.grid(True)
   
fig.autofmt_xdate()
   
fig.suptitle('matplotlib.figure.Figure.autofmt_xdate() \
function Example\n\n', fontweight ="bold")
  
plt.show()