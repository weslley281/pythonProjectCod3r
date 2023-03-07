def age_group(age_informed: int):
    if 0 <= age_informed < 18:
        return 'Minor'
    elif age_informed in range(18, 64):
        return "Adult"
    elif age_informed in range(65, 100):
        return "Best age"
    elif age_informed >= 100:
        return  "centenary"
    else:
        return "invalid age"


if __name__ == '__main__':
    for age in (17, 35, 87, 113, -15):
        print(f"{age}: {age_group(age)}")