#import statements
import pandas as pd
from shiny.express import ui, render, input
import plotly.express as px
from shinywidgets import render_widget 
from shiny import reactive, render
import faicons as fa

#loading the dataset
df = pd.read_csv("nba_players.csv")
years = sorted(df["season"].unique())

#side bar
with ui.sidebar(position="left", open="open"):
    with ui.div(style="display: flex; justify-content: flex-end;"):
        ui.input_dark_mode() 
    ui.input_selectize("Year", "Select The Year", choices=years, selected="2008-09")

#styling 
ui.tags.style(
    """
    .stat-card {
        background: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        text-align: center;
        width: 260px;
        margin-bottom: 15px;
    }

    .stat-title {
        font-size: 18px;
        font-weight: 600;
        color: #333;
        margin-bottom: 10px;
    }

    .stat-value {
        font-size: 18px;
        font-weight: bold;
        color: #2a6df4;
    }
    .nav-spacing {
        margin-top: 15px;
    }
    .Space{
        margin:15px 10px;
    }
    .title{
        font-weight:750;
        color:#2a6df4;
    }
    .center{
        display:flex;
        justify-content:center;
        padding:5px;
    }
    
    """
)

#rendering the ui
@render.express
def player_cards():
    with ui.div(class_="center"):
         ui.h3("NBA Analysis 1996-2023",class_="title")
    show = df[df["season"] == input.Year()]
    s = show.loc[show["pts"].idxmax()]
    with ui.layout_column_wrap():
        with ui.card(class_="stat-card"):
                ui.h4("Most Games Played In Season", class_="stat-title")
                ui.p(f"{show.loc[show['gp'].idxmax()]['player_name']} - ({show.loc[show['gp'].idxmax()]['gp']})",
                    class_="stat-value")

        with ui.card(class_="stat-card"):
                ui.h4("Highest Avg Points in Season by Player", class_="stat-title")
                ui.h6(f"{show.loc[show['pts'].idxmax()]['player_name']} - ({show.loc[show['pts'].idxmax()]['pts']})",
                    class_="stat-value")

        with ui.card(class_="stat-card"):
                ui.h4("Highest Avg Assits in Season by Player", class_="stat-title")
                ui.h6(f"{show.loc[show['ast'].idxmax()]['player_name']} - ({show.loc[show['ast'].idxmax()]['ast']})",
                    class_="stat-value")

        with ui.card(class_="stat-card"):
                ui.h4("Highest Net Rating of Player", class_="stat-title")
                ui.h6(f"{show.loc[show['net_rating'].idxmax()]['player_name']} - ({show.loc[show['net_rating'].idxmax()]['net_rating']})",
                    class_="stat-value")
    #nav_bar
    with ui.div(class_="nav-spacing"):
        with ui.navset_pill():
            #avg_points_per_team
            with ui.nav_panel("A"):
                with ui.card(class_="Space"):
                     @render_widget
                     def team_avg_plot():
                        team_avg = round(show.groupby("team_abbreviation", as_index=False)["pts"].mean(),2)
                        team_avg=team_avg.sort_values(by="pts",ascending=False)
                        team_avg = team_avg.rename(columns={"pts": "average_pts"})
                        fig = px.bar(
                            team_avg,
                            x="team_abbreviation",
                            y="average_pts",
                            title=f"Avg Points of Teams In Season {input.Year()}",
                        )
                        fig.update_layout(
                            plot_bgcolor="#ffffff",
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600),
                        )
                        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="white")
                        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="white") 
                        return fig
                
                compare=df[df["season"] != input.Year()]
                compare=compare["season"].drop_duplicates()
                print(list(compare))
                with ui.card(class_="Space"):
                    with ui.div(style="display: flex; justify-content: space-between; align-items: center; gap: 20px;"):
                        ui.input_selectize("Compare", "Select The Year", choices=list(compare), selected="2008-09")
                        ui.input_action_button("action_button", "Compare",)
                    @render_widget
                    @reactive.event(input.action_button)
                    def team_avg_2():
                        cd = df[df["season"] == input.Compare()]
                        team_avg2 = round(cd.groupby("team_abbreviation", as_index=False)["pts"].mean(),2)
                        team_avg2=team_avg2.sort_values(by="pts",ascending=False)
                        team_avg2 = team_avg2.rename(columns={"pts": "average_pts"})
                        fig = px.bar(
                            team_avg2,
                            x="team_abbreviation",
                            y="average_pts",
                            title=f"Avg Points of Teams In Season {input.Compare()}",
                        )
                        fig.update_layout(
                            plot_bgcolor="#ffffff",
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600),
                        )
                        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="white")
                        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="white") 
                        return fig
                    
            #Player from complete world                          
            with ui.nav_panel("B"):
                with ui.card(class_="Space"):
                     @render_widget
                     def map():
                        country_counts = show.groupby("country").size().reset_index(name="player_count")
                        fig = px.choropleth(
                            country_counts,
                            locations="country",              
                            locationmode="country names",     
                            color="player_count",
                            title=f"Number of Players by Country In Season {input.Year()}",
                            color_continuous_scale="thermal",
                        )

                        fig.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                            )
                        return fig
                     
                with ui.card(class_="Space"):
                    with ui.div(style="display: flex; justify-content: space-between; align-items: center; gap: 20px;"):
                        ui.input_selectize("getYear","Select the year",list(compare),selected="2009-10")
                        ui.input_action_button("comp1","Compare")
                    @render_widget
                    @reactive.event(input.comp1)
                    def map1():
                        print(input.getYear())
                        mappy=df[df["season"] == input.getYear()]
                        print(mappy)
                        country2=mappy.groupby("country").size().reset_index(name="player_count")
                        fig = px.choropleth(
                            country2,
                            locations="country",              
                            locationmode="country names",     
                            color="player_count",
                            title=f"Number of Players by Country In Season {input.getYear()}",
                            color_continuous_scale="thermal",
                        )
                        fig.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                            )
                        return fig        
            #Scatter plot of the usg and avg points    
            with ui.nav_panel("C"):
                with ui.card(class_="Space"):
                    @render_widget
                    def graph3():
                        fig3 = px.scatter(
                            show,
                            x=show["usg_pct"]*100,
                            y="pts",
                            title="Usage percentage vs Avg points",
                            labels={
                                "x": "USG (%)",
                                "pts": "Avg Points"
                            }
                        )
                        fig3.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                        )
                        return fig3
                    
                with ui.card(class_="Space"):
                    with ui.div(style="display: flex; justify-content: space-between; align-items: center; gap: 20px;"):
                        ui.input_selectize("gety","Select the Year", list(compare), selected="2004-05")
                        ui.input_action_button("comp2","compare")
                    
                    @render_widget
                    @reactive.event(input.comp2)
                    def graph3c():
                        sactty=df[df["season"] == input.gety()]
                        fig3 = px.scatter(
                            sactty,
                            x=sactty["usg_pct"]*100,
                            y="pts",
                            title="Usage percentage vs Avg points",
                            labels={
                                "x": "USG (%)",
                                "pts": "Avg Points"
                            }
                        )
                        fig3.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                        )
                        return fig3
                    
            #player performance        
            with ui.nav_panel("D"):

                players = df["player_name"].drop_duplicates().astype(str).tolist()
                ui.input_selectize(
                    id="player",
                    label="Select the Player",
                    choices=players,
                    selected="Erick Dampier"
                )
                with ui.card():
                    @render_widget
                    def line1():
                        print("Selected =", (input.player()))
                        stats = df[df["player_name"] == str(input.player())]

                        fig3 = px.line(
                            data_frame=stats,
                            x="season",
                            y="pts",
                            markers=True,
                            title="AVG Points By Player Over The Seasons",
                            labels={
                                "season":"Seasons",
                                "pts":"AVG Points"
                            }
                        )
                        fig3.update_xaxes(
                        type='category',
                        categoryorder='array',
                        categoryarray=stats["season"]
                        )
                        fig3.update_yaxes(
                            range=[0,df["pts"].max()]
                        )
                        fig3.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                        )
                        return fig3
                
                with ui.card():
                    @render_widget
                    def line2():
                        print("Selected =", (input.player()))
                        stats = df[df["player_name"] == str(input.player())]
                        fig4 = px.line(
                            data_frame=stats,
                            x="season",
                            y="reb",
                            markers=True,
                            title="AVG Rebounds By Player Over The Seasons",
                            labels={
                                "season":"Seasons",
                                "reb":"AVG Rebounds"
                            }
                        )
                        fig4.update_xaxes(
                        type='category',
                        categoryorder='array',
                        categoryarray=stats["season"]
                        )

                        fig4.update_yaxes(
                            range=[0,df["reb"].max()],
                        )
                        fig4.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                        )
                        return fig4
                    
                with ui.card():
                     @render_widget  
                     def line3():
                        print("Selected =", (input.player()))
                        stats = df[df["player_name"] == str(input.player())]
                        print(stats)

                        fig5 = px.line(
                            data_frame=stats,
                            x="season",
                            y="ast",
                            markers=True,
                            title="AVG Assits By Player Over The Seasons",
                            labels={
                                "season":"Seasons",
                                "ast":"AVG Assits"
                            }
                        )

                        fig5.update_xaxes(
                        type="category",
                        categoryorder='array',
                        categoryarray=stats["season"]
                        )
                        fig5.update_yaxes(
                            range=[0, df["ast"].max()]
                        )   
                        fig5.update_layout(
                            margin=dict(l=0, r=0, t=40, b=0),
                            title_x=0.5,
                            title_font=dict(size=20, color="#2a6df4",weight=600)
                        )    
                        return fig5