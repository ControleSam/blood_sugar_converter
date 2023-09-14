import streamlit as st

st.markdown(
    """
                # Blood sugar level converter

                This simple app converts the blood sugar level from **mg/dL** to **mmol/L**, and vice versa. Simply insert the measure of the your blood sugar in the appropriate field and you will have the converted measure in the other field.
                
                """
)

st.write('<hr style="border:2px solid gray">', unsafe_allow_html=True)

generalInfo = "In general, the normal range for blood sugar may vary depending on you diabetes status, on the time of day, whether before or after meals."


def giveInfo():
    # with infos:
    if st.session_state.mg < 70:
        st.error(
            "Your blood sugar level may be **too low**. Consult your doctor about this.",
            icon="🚨",
        )
    elif st.session_state.mg > 130 and st.session_state.when == "Before meals":
        st.error(
            "Your blood sugar level may be **too high**. Consult your doctor about this.",
            icon="🚨",
        )
    elif st.session_state.mg > 180 and st.session_state.when == "After meals":
        st.error(
            "Your blood sugar level may be **too high**. Consult your doctor about this.",
            icon="🚨",
        )
    else:
        st.balloons()
        st.success("Your blood sugar level is within normal range :clap:.", icon="✅")

    st.info(generalInfo, icon="ℹ️")


def timeChange():
    if not st.session_state.get("when"):
        st.session_state.when = when
    else:
        giveInfo()


def mmol2mg():
    st.session_state.mg = st.session_state.mmol / 0.0555
    st.session_state.whochanged = "mmol/L"
    giveInfo()


def mg2mmol():
    st.session_state.mmol = st.session_state.mg * 0.0555
    st.session_state.whochanged = "mg/dL"
    giveInfo()


st.write(
    "<style>div.block-container{padding-top: 2rem;}</style>",
    unsafe_allow_html=True,
)
# st.write(
#     "<style>h3{padding-top: 1rem;}</style>",
#     unsafe_allow_html=True,
# )
when = st.radio(
    "Time of measurement:",
    ["Before meals", "After meals"],
    horizontal=True,
    key="when",
    on_change=timeChange,
)
st.markdown("---")
# if not st.session_state.get("when"):
#     st.session_state.when = when

mgPerdLCol, _, mmolPerLCol = st.columns([4, 1, 4])

infos = st.expander("Remark", expanded=True)

with mgPerdLCol:
    st.subheader("mg/dL")
    mgPerdL = st.number_input("", key="mg", on_change=mg2mmol)

with mmolPerLCol:
    st.subheader("mmol/L")
    mmolPerL = st.number_input("", key="mmol", on_change=mmol2mg)


# ---------- footer-------------
# taken from https://discuss.streamlit.io/t/st-footer/6447
from htbuilder import (
    HtmlElement,
    div,
    ul,
    li,
    br,
    hr,
    a,
    p,
    img,
    styles,
    classes,
    fonts,
)
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):
    style = """
    <style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800;900&display=swap");
   
    # MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    #  .stApp { bottom: 25px; font-family:"Poppins", sans-serif;}
    </style>
    """

    style_div = styles(
        # position="-webkit-sticky",
        position="fixed",
        left=0,
        bottom=0,
        # margin=px(0, 0, 0, 0),
        padding=px(10, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="50px",
        opacity=1,
        background_color="#24262b",  #'#457b9d'
    )

    style_hr = styles(
        display="block",
        margin=px(0, 0, "auto", "auto"),
        border_style="solid",
        border_width=px(1),
        border_color="#F0F2F6",
    )

    body = p()
    foot = div(style=style_div)(
        # hr(
        #     style=style_hr
        # ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "This Conversion App was built with",
        image(
            "https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg",
            width=px(25),
            height=px(25),
        ),
        " and ",
        image(
            "https://streamlit.io/images/brand/streamlit-mark-color.svg",
            width=px(25),
            height=px(25),
        ),
        " by ",
        link("https://github.com/ControleSam", "Samuel Ntim"),
        # br(),
        # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)


footer()
