import datetime
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

# import tzlocal
# from astral import Astral
# from pytz import timezone

__author__ = `dladd10`

class GoodMorningSkill(MycroftSkill):
    def __init__(self):
        super(GoodMorningSkill, self).__init__(name="GoodMorningSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

	#.voc files
        GoodMorningIntent = IntentBuilder("GoodMorningIntent").require("GoodMorning").build()
	self.register_intent(good_morning_intent, self.handle_good_morning_reply_intent)

    #What Mycroft is to do
    def handle_good_morning_reply_intent(self, message):
	#Say Good Morning
	self.speak_dialog("GoodMorningKeywords")
	#Tell you the date
	##todaydate = datetime.datetime.now().strftime("%B %d, %Y")
	##today = datetime.datetime.strptime(todaydate, '%B %d, %Y').strftime('%A')


	#location = message.metadata.get("Location", None)

	#now = datetime.datetime.now(timezone('UTC'))
	#if location is None:
	#    tz = tzlocal.get_localzone()
	#else:
	#    astral_tz = self.get_timezone(location)
	#    tz = timezone(astral_tz) if astral_tz else None
	#    if not tz:
	#        self.speak("I could not find the timezone for " + location)
	#	return

	#time_value = today
	##self.speak("Today is " + today)


    def stop(self):
        pass

def create_skill():
    return GoodMorningSkill()
