class SigninLocator(object):
    signin_btn_xpath = "/html/body/div/div/div[1]/header/div/div/div[2]/ul/li[3]/a"
    email_input_id = "form_login-email"
    password_input_id = "form_login-password"
    submit_btn_id = "form_login-submit"


class SignupLocators(object):
    signin_btn_xpath = "/html/body/div/div/div[1]/header/div/div/div[2]/ul/li[3]/a"
    signup_btn_xpath = "/html/body/div/div/div[1]/header/div/div/div[4]/div[1]/div[2]/a[1]"
    email_inputId = "form_register-email"
    name_inputId = "form_register-name"
    pass_inputId = "form_register-password"
    repass_inputId = "form_register-password2"
    signup_sub_btnId = "form_register-submit"


class SigninWithGoogleLocators(object):
    signinBtnXpath = "/html/body/div/div/div[1]/header/div/div/div[2]/ul/li[3]/a"
    googleBtnId = "google-sign-in"
    emailX = '//*[@id="identifierId"]'
    nextbtnX = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
    passX = "password"
    subbtnX = '//*[@id="passwordNext"]/div/button/div[2]'


class GetHotel(object):
    hotelBtnId = "button-hotels"
    hotellocationXpath = '//*[@id="hotels-from"]'
    checkinDateXpath = '/html/body/div[1]/div/section[1]/div[2]/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[1]/a'
    checkinDateSelectXpath = '/html/body/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[10]'
    searchBtnId = "hotel-search"

    nextPageXpath = '/html/body/header/nav/div[2]/div[6]/a'
    see_abilityXpath = '//*[@id="search_results_table"]/div[1]/div/div/div/div[5]/div[1]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/a'
    resurbe_hotelXpath = '//*[@id="hcta"]'


class GetTicketLocatros(object):
    BtnId = "button-tickets"
    tinputfromXpath = "tickets-from"
    InputToXpath = "tickets-to"
    depatureDateXpath = '/html/body/div[1]/div/section[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a'
    DtateselectX = '/html/body/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[11]'
    returndateX = '/html/body/div[1]/div/section[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/a'
    returndateselectX = '/html/body/div[3]/div/div/div/div/div/div[2]/div/div[5]/div[25]'
    searcbtnX = '//*[@id="ticket-search"]'


class GetCarLocators(object):
    carBtnId = "button-cars"
    carsfromId = "cars-from"
    carsearchId = 'car-search'


















