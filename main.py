import sys, argparse, qrcode
from qrcode.image.pure import PyPNGImage

from gettext import gettext as _


class TXTFileType(argparse.FileType):
    def __call__(self, string: str):
        if not string.endswith(".txt"):
            args = {"file": string}
            message = _("Kiritilgan fayl turi .txt emas: '%(file)s'")
            raise argparse.ArgumentTypeError(message % args)
        return super().__call__(string)


def read_file(file: TXTFileType) -> list:
    file = file.readlines()
    lines = [line.rstrip("\n") for line in list(file)]
    return lines


def qr_code_generator(file: TXTFileType, box_size: int, border: int, image_factory):
    if box_size <= 0 and border <= 0:
        raise ValueError(
            f"box_size va border 0 dan kichik qiymat qabul qila olmaydi: {box_size}, {border}"
        )
    if box_size <= 0:
        raise ValueError(f"box_size 0 dan kichik qiymat qabul qila olmaydi: {box_size}")
    if border <= 0:
        raise ValueError(f"border 0 dan kichik qiymat qabul qila olmaydi: {border}")

    lines = read_file(file)
    for line in lines:
        qr = qrcode.QRCode(box_size=box_size, border=border)
        qr.add_data(line, 0)
        img = qr.make_image(image_factory=image_factory)
        img.save(f"images/{line}.png")


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        prog="QR code generator",
        description="`QR code` generatsiya qiluvchi terminalda ishlovchi kichik dastur",
        epilog="Muallif: Jahongir Qurbonov",
    )
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "-f",
        "--file",
        default="data.txt",
        type=TXTFileType(),
        # required=True,
        # help="Ma'lumotlar joylangan .txt kengaytmali faylni to'liq nomini ko'sating",
    )
    parser.add_argument("--box_size", default=10, type=int, help="")
    parser.add_argument("--border", default=4, type=int, help="")
    parser.add_argument("--image_factory", default=PyPNGImage)
    args = parser.parse_args(argv)
    try:
        qr_code_generator(args.file, args.box_size, args.border, args.image_factory)
    finally:
        print("=> QR kodlar muvaffaqiyatli generatsiya qilindi!")


if __name__ == "__main__":
    main()
