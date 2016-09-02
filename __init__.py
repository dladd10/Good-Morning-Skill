from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import datetime
# import tzlocal
# from astral import Astral
# from pytz import timezone

#__author__ = `dladd10`

LOGGER = getLogger(__name__)

class GoodMorningSkill(MycroftSkill):

    def __init__(self):
        super(GoodMorningSkill, self).__init__(name="GoodMorningSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

		#.voc files
        goodmorningintent = IntentBuilder("GoodMorningIntent").\
            require("goodmorningkeyword").build()

        self.register_intent(goodmorningintent, self.handle_goodmorningintent)

    #What Mycroft is to do
    def handle_goodmorningintent(self, message):
        # TODO Say Good Morning
        self.speak_dialog("GoodMorningReply")

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
