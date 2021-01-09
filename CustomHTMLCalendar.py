from IPython.display import Markdown as md
from calendar import HTMLCalendar
from datetime import datetime, timedelta
import sys
from dateutil.relativedelta import relativedelta


class CustomHTMLCalendar(HTMLCalendar):
    """
    Custom class to print out HTML calendar for given number of days. The class
    creates <href> tag for days falling between the said range.
    """

    def __init__(self, start_date, num_of_days):
        """
        start_date: YYYY-MM-DD, count days starting from this date
        num_of_days: number of days to display
        """
        super().__init__(0)
        self.start_date = start_date
        self.num_of_days = num_of_days
        self.start_date_fmt = "%Y-%m-%d"

        try:
            self.start_date_formatted = datetime.strptime(
                self.start_date, self.start_date_fmt
            )
        except ValueError:
            print("Start date is in invalid format. Need YYYY-MM-DD format.")
            raise
        except Exception as e:
            print("Error in date conversion, please check: ", e)
            raise
        else:
            self.dd = self.start_date_formatted.day
            self.month = self.start_date_formatted.month
            self.year = self.start_date_formatted.year

            self.end_date = self.start_date_formatted + timedelta(
                days=self.num_of_days
            )
            print(f"The end date is {self.end_date}")

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        # print(day, "====> ", self._curr_date.day, self._curr_date.month,
        # self._curr_date.year)
        if day != 0:
            self._print_date = datetime(
                self._curr_date.year, self._curr_date.month, day
            )
            self.link = "https://github.com/kpimparkar/66daysDS"
        if day == 0:
            # day outside month
            return '<td class="noday">&nbsp;</td>'
        elif (
            self._print_date >= self.start_date_formatted
            and self._print_date <= self.end_date
        ):
            # day with the date range
            return '<td class="{}"><strong><a href={}; style="background-color:MediumSeaGreen; color:white;font-size:150%;" target="_blank">{}</a></strong></td>'.format(
                self.cssclasses[weekday], self.link, day
            )
        else:
            # day outside of the daterange
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def show_calendar(self):
        """
        Prints out HTML calendar for the months involved in the provided
        duration. Days falling in the range get a <href> tag with a predefined
        link.
        """
        self._curr_date = self.start_date_formatted

        while self._curr_date < self.end_date:
            if (
                self._curr_date.month == self.end_date.month
                and self._curr_date.year == self.end_date.year
            ):
                # print(self._curr_date)
                print(
                    self.formatmonth(
                        self._curr_date.year, self._curr_date.month
                    )
                )
                break
            else:
                # print(self._curr_date)
                print(
                    self.formatmonth(
                        self._curr_date.year, self._curr_date.month
                    )
                )
            self._curr_date += relativedelta(months=1)


if __name__ == "__main__":
    myCal = CustomHTMLCalendar(start_date="2021-01-07", num_of_days=66)
    myCal.show_calendar()