style = f'''
#Tray {{
    
}}

#TrayActive {{
    background-color: black;
}}

#Menu {{
    background-color: black;
}}

#Slider {{
    min-height: 30px;
    min-width: 200px;
}}

#Slider::groove:horizontal {{
    background-color: gray;
    border: 1px solid;
    height: 6px;
    margin: 0px;
}}
    
#Slider::handle:horizontal {{
    background-color: white;
    width: 10px;
    margin: -10px 0px;
}}

#Slider::handle:horizontal:hover {{
    background-color: darkgray;
}}

#Button {{
    background-color: transparent;
    border: none;
    min-width: 50px;
    color: white;
    font-size: 18px;
    font-weight: bold;
}}

#Button:hover {{
    font-size: 22px;
}}

#Menu::item {{
    color: white;
    font-size: 16px;
    padding: 5px;
    min-width: 75px;
}}

#Menu::item:selected {{  /* hover */
    background-color: rgba(255, 255, 255, 0.2);
}}
'''
