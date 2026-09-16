# Legacy bank login code

def bank_login(account_holder, pin):
    if account_holder == "Aisha" and pin == "4826":
        print("ok")
        return True
    print("fail")
    return False


bank_login("Aisha", "4826")
