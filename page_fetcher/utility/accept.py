# https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values

# fmt: off
FIREFOX_DEFAULT_ACCEPTS = (
    ("92.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    ("72.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("66.0", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("65.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("0.0", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
)

FIREFOX_IMAGE_ACCEPTS = (
    ("92.0", "image/avif,image/webp,*/*"),
    ("65.0", "image/webp,*/*"),
    ("47.0", "*/*"),
    ("0.0", "image/png,image/*;q=0.8,*/*;q=0.5"),
)

FIREFOX_VIDEO_ACCEPTS = (
    ("3.6", "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5"),
)

FIREFOX_AUDIO_ACCEPTS = (
    ("3.6", "audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5"),
)

FIREFOX_SCRIPT_ACCEPTS = (
    ("0.0", "*/*"),
)

FIREFOX_CSS_ACCEPTS = (
    ("4.0", "text/css,*/*;q=0.1"),
)

FIREFOX_ACCEPTS = {
    "default": FIREFOX_DEFAULT_ACCEPTS,
    "image": FIREFOX_IMAGE_ACCEPTS,
    "video": FIREFOX_VIDEO_ACCEPTS,
    "script": FIREFOX_SCRIPT_ACCEPTS,
    "css": FIREFOX_CSS_ACCEPTS,
}

CHROME_DEFAULT_ACCEPTS = (
    ("97.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"),
    ("0.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
)

CHROME_IMAGE_ACCEPTS = (
    ("97.0", "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"),
    ("0.0", "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"),
)

CHROME_VIDEO_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_AUDIO_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_SCRIPT_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_CSS_ACCEPTS = (
    ("0.0", "text/css,*/*;q=0.1"),
)

CHROME_ACCEPTS = {
    "default": CHROME_DEFAULT_ACCEPTS,
    "image": CHROME_IMAGE_ACCEPTS,
    "video": CHROME_VIDEO_ACCEPTS,
    "audio": CHROME_AUDIO_ACCEPTS,
    "script": CHROME_SCRIPT_ACCEPTS,
    "css": CHROME_CSS_ACCEPTS,
}

IE_DEFAULT_ACCEPTS = (
    ("0.0", "image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*"),
)

IE_IMAGE_ACCEPTS = (
    ("9.0", "image/png,image/svg+xml,image/*;q=0.8, */*;q=0.5"),
    ("0.0", "*/*"),
)

IE_SCRIPT_ACCEPTS = (
    ("9.0", "application/javascript, */*;q=0.8"),
    ("0.0", "*/*"),
)

IE_CSS_ACCEPTS = (
    ("9.0", "text/css"),
)

IE_ACCEPTS = {
    "default": IE_DEFAULT_ACCEPTS,
    "image": IE_IMAGE_ACCEPTS,
    "video": IE_DEFAULT_ACCEPTS, # no support
    "audio": IE_DEFAULT_ACCEPTS, # no support
    "script": IE_SCRIPT_ACCEPTS,
    "css": IE_CSS_ACCEPTS,
}
# fmt: on


def get_version_accept(build_version: str, accepts: tuple) -> str:
    for version, accept in accepts:
        if build_version > version:
            return accept
    return None


def get_firefox_accept(version: str, context: str) -> str:
    return (
        get_version_accept(version, FIREFOX_ACCEPTS[context])
        or get_version_accept(version, FIREFOX_DEFAULT_ACCEPTS)
        or "*/*"
    )


def get_chrome_accept(version: str, context: str) -> str:
    return (
        get_version_accept(version, CHROME_ACCEPTS[context])
        or get_version_accept(version, CHROME_DEFAULT_ACCEPTS)
        or "*/*"
    )


def get_ie_accept(version: str, context: str) -> str:
    return (
        get_version_accept(version, IE_ACCEPTS[context])
        or get_version_accept(version, IE_DEFAULT_ACCEPTS)
        or "*/*"
    )


def generate_accept(navigator: str, version: str, context: str = "default") -> str:
    match navigator:
        case "firefox":
            return get_firefox_accept(version, context)
        case "chrome":
            return get_chrome_accept(version, context)
        case "ie":
            return get_ie_accept(version, context)
    raise Exception("Unknow navigator")
