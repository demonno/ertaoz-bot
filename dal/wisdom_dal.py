import random

from dal.models import Wisdom


class WisdomDal:
    WISDOM_LIST = [
        Wisdom(
            text="სიყვარული ვერტიკალურია და თან ბრუნვადი",
            animation="https://s4.gifyu.com/images/love.gif",
        ),
        Wisdom(
            text="არა, ყმაწვილო, არა! ასეთი ცოდნით ვერ გავფრინდებით, "
            "არადა, უნდა გავფრინდეთ!",
            animation="https://thumbs.gfycat.com/AdventurousColossalBobwhite-size_restricted.gif",
        ),
        Wisdom(
            text="რომელია ჩვენს შორის მართალი, იქ გამოჩნდება, ზეცაში!",
            animation="https://thumbs.gfycat.com/RelievedSardonicGoa-size_restricted.gif",
        ),
        Wisdom(
            text=(
                "სიყვარული... სიყვარულია მშობელი ოცნებისა, "
                "ოცნება აღვიძებს კაცთა მოდგმის მთვლემარე გონებას, "
                "გონება აღძრავს ქმედებას, პლიუს-მინუს, ემ ცე კვადრატ (mc²), "
                "ეф, ფუძე (√) ვნებათაღელვის უსასრულობისა და "
                "შეცნობილი აუცილებლობისაკენ! მიდით ერთაოზ!"
            ),
            animation="https://i.makeagif.com/media/7-09-2015/gLIbf3.gif",
        ),
    ]

    def fetch_random(self) -> Wisdom:
        return random.choice(self.WISDOM_LIST)
