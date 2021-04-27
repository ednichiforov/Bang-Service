from io import BytesIO
import qrcode
from django.contrib.sites.models import Site
from .models import UsersStartedConv


current_site = Site.objects.get_current()
website = current_site.domain


def qr_code_image(update):
    """ Makes QR code """

    user = update.message.from_user
    user_id = UsersStartedConv.objects.values("user_id").get(user_id=user.id)["user_id"]
    input_data = website + "/users/" + str(user_id)

    pillow_image = qrcode.make(input_data)

    byteImgIO = BytesIO()
    byteImgIO.name = str(user_id) + ".jpeg"
    pillow_image.save(byteImgIO, "JPEG")
    byteImgIO.seek(0)

    return byteImgIO
