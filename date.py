def date():
    """
    get today's date
    """

    # Import date class from datetime module
    from datetime import date

    # Returns the current local date
    today = date.today()
    # print("Today date is: ", today)
    today=str(today)
    return today
