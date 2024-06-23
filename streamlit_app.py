import streamlit as st
import folium
import pandas as pd
import io 

def dados():  
    data = pd.read_excel('valor.xlsx')
    st.header('Download Dados', divider='red')
    st.dataframe(data)
    if st.button('Solicitar dados'):
        df = data.copy()
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, header=True)
        excel_data = excel_buffer.getvalue()
        st.download_button("Baixe os valores de 15 dias", excel_data, file_name='Dados_UCs.xlsx')
    else:
         st.warning("Sem dados para baixar")
def Mapa():   
    from streamlit_folium import st_folium  
    st.header('Mapa das Unidades', divider='red')  
    # Cria o mapa centralizado em uma localização específica
    m = folium.Map(location=(-3.71839, -38.5434))

    #! ULTRAPASSADOS

    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.7997058197269378, -40.25621828676672],
        tooltip="1017401",
        popup="ETA - FORQUILHA",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

    folium.Marker(
        location=[-5.463787529458468, -40.78005110289483],
        tooltip="9009221",
        popup="ETA - NOVO ORIENTE",
        icon=folium.Icon(icon="fire", color='red'),
    ).add_to(m)
    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.829556919772068, -38.557312423271],
        tooltip="9003917",
        popup="SEDE ADMINISTRATIVA DA UNMTS",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-6.7272835029943625, -38.715568213490656],
        tooltip="9009457",
        popup="SSD-01 DO SI BAIXIO",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.970218235400555, -37.97638711534415],
        tooltip="9001789",
        popup="CS-01 + CSB-01 DO SAA RUSSAS",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.49034751474691, -38.5963726386168],
        tooltip="9011318",
        popup="CS-02 + EEAB-02 DO SI OCARA",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.694321662853855, -38.039499553026694],
        tooltip="9006300",
        popup="EEAB-02 DO SAA PALHANO",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-5.613291822298348, -38.76342058218057],
        tooltip="52392974",
        popup="CS-02 DO SAA JAGUARETAMA",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.23022923908172, -39.32172410613558],
        tooltip="9011153",
        popup="CSB-44 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.09155079456411, -40.02843112304951],
        tooltip="9001452",
        popup="CS-01 + ETA POTENGI DO SAA POTENGI",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.178427290708941, -38.86420648158024],
        tooltip="430035",
        popup="CSB-15 + CSB-19 + ETA PACOTI DO SAA ",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.24121298878452, -39.27958192822686],
        tooltip="57654978",
        popup="SSD-38 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.24088868219311, -39.31288428548631],
        tooltip="9004223",
        popup="CSB-08 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="fire", color='red'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.035822476465559, -41.240443822766395],
        tooltip="9001931",
        popup="CS-01 + ETA CHAVAL",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# SEM TELEMETRIA

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.8299449952584625, -39.066130760625356],
        tooltip="9001614",
        popup="SSD-01 DO SAA PENAFORTE",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.538486546727683, -40.45857005867043],
        tooltip="9011108",
        popup="CS-03 (AÇUDE JENIPAPO) - MERUOCA",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-5.194720954121337, -40.65741171036],
        tooltip="1525146",
        popup="CS-01 (BARRAGEM DO RIO POTY) - CRATEÚS",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-6.98231141217335, -39.715949316061],
        tooltip="1814261",
        popup="EEAB-01 / RAP-01 (ALTANEIRA)",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-5.271106076454046, -40.66838884132236],
        tooltip="24444213",
        popup="CS-02 (EECS-02B - AÇUDE ",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-6.177118705578564, -39.90227596281519],
        tooltip="9003497",
        popup="CSB-04 + CSB-05 + CSB-06 + SSD-04 ",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-5.8920078717565785, -38.62193137103304],
        tooltip="40757962",
        popup="EEAB-03 (AQUINÓPOLIS - JAGUARIBE)",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.451999689328035, -38.15944470734253],
        tooltip="32649938",
        popup="CS-01 + CSB-01 + ETA SERRA DO FÉLIX ",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.663010386498672, -40.483970195019644],
        tooltip="1780598",
        popup="CS-01 + EEAB-01 (RIO COREAÚ)",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-7.208721840829631, -39.31576754288003],
        tooltip="671944",
        popup="CSB-06 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="lock", color='gray'), 
    ).add_to(m)

#* OK

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-5.2127108233333175, -38.13521869754026],
        tooltip="1053122",
        popup="CS-01 + ETA TABULEIRO DO NORTE",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)

    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.896925321562796, -38.650295228769664],
        tooltip="672007",
        popup="PT-02 / MED-02 (BARBALHA)",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)

    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.7259798861523805, -38.47517903873921],
        tooltip="9001387",
        popup="UTR-08 + BOOSTER SÃO PEDRO + ",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)
    
    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-6.2166136468534114, -40.703589401156236],
        tooltip="9008613",
        popup="CS-02 (AÇUDE FACUNDO)",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)

     # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.7714372897909243, -38.535492060673164],
        tooltip="1578819",
        popup="SEDE ADMINISTRATIVA DA CAGECE",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)

     # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.7588270222285414, -38.57485111516948],
        tooltip="521852",
        popup="CAGECE PICI",
        icon=folium.Icon(icon="user", color='green'), 
    ).add_to(m)

   
    # Exibe o mapa no Streamlit
    st_folium(m, width=700, height=500)



if __name__ == "__main__":
    st.sidebar.title("Navegação")
    opcoes = ["Página Inicial", "Dados"]
    escolha = st.sidebar.selectbox("Escolha uma página", opcoes) #radio 

    if escolha == "Página Inicial":
        Mapa()    
    elif escolha == "Dados":
        dados()

    #Mapa()

    

    
