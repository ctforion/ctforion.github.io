# UT.js Manual
# Tracker for ctforion.com
# Developed by: Unkn0wn2603
# Description:
#   This file defines the constants and keyword rules used by UT.js.
#   UT.js is a tracking solution designed to monitor performance
#   and capture event data efficiently for ctforion.com.
# Creation Date: January 26, 2025


UT_KEY = { 
    "ACTIVITY_TYPE" : {
        "0"  : "end",
        "1"  : "start",
        "c"  : "click",
        "d"  : "download",
        "e"  : "error",
        "f"  : "focus",
        "h"  : "hover",
        "i"  : "idle",
        "r"  : "reconnect",
        "s"  : "scroll",
        "u"  : "upload",
        "v"  : "visibility",
        "lt" : "load_time",
        "fc" : "focus_change",
        "vc" : "visibility_change",
        "fs" : "form_submit",
        "is" : "idle_start",
        "ie" : "idle_end",
        "id" : "input_data",
        "ic" : "input_complete",
        "kp" : "key_press",
        "po" : "page_open",
        "pc" : "page_close",
        "er" : "error_reject",
        "do" : "device_orientation",
        "dm" : "device_motion",
    },
    
    "CONTENT_VALUE_TYPE" : {
        "0"       : False,
        "1"       : True,
        
        "T"       : True,
        "F"       : False,
        
        "visible" : True,
        "hidden"  : False,
        
        "N"       : None, 
        "O"       : None,
        "E"       : "",
        
        
    },
    "CONTENT_TYPE" : { 
        # those things accessable jsonbody["D"]...
        "0"   : "things_are_endings",
        "1"   : "things_are_starting",
        
        # CHAPITAL SINGLE LETTERED KEYS ARE USED FOR TRACKING
        "D"   : "data",
        "M"   : "message",
        "N"   : "filename",
        "S"   : "source",
        "T"   : "time",
        "U"   : "URL",
        "R"   : "referrer_url",
        "E"   : "element",
        "L"   : "line",
        "I"   : "id",
        "K"   : "key",
        "V"   : "value",
        "O"   : "opening",
        "C"   : "closing",
        
        # SMALL SINGLE LETTERED KEYS ARE USED FOR TRACKING
        "a"   : "alpha",
        "b"   : "beta",
        "g"   : "gamma",
        
        # SMALL DOUBLE LETTERED KEYS ARE USED FOR TRACKING
        "cc"  : "click_count",
        "et"  : "element_type",
        
        
        "oX"  : "orientation_x",
        "oY"  : "orientation_y",
        "oZ"  : "orientation_z",
        "aX"  : "acceleration_x",
        "aY"  : "acceleration_y",
        "aZ"  : "acceleration_z",
        "rA"  : "rotation_alpha",
        "rB"  : "rotation_beta",
        "rG"  : "rotation_gamma",
        
        "st"  : "status",
        "ec"  : "event_code",
        "pt"  : "page_title",
        "pl"  : "page_link",
        "ln"  : "line",
        "cl"  : "column",
        "sk"  : "stack",
        "fn"  : "filename",
        "ft"  : "filetype",
        "rs"  : "reason",
        "fi"  : "form_id",
        
        # SMALL TRIPLE LETTERED KEYS ARE USED FOR TRACKING
        
        "elt" : "element_text",
        "elh" : "element_html",
        "elc" : "element_class",
        "elh" : "element_href",
        "els" : "element_src",
        "elv" : "element_value",


        "sdp" : "scroll_depth",
        "sdr" : "scroll_direction",
        "scp" : "scroll_position",
        "plt" : "page_load_time",
        "idt" : "idle_duration_time",
        "lcf" : "largestcontentfulpaint", # THIS PRESENTS LARGE CONTENTFUL PAINT
        "nvs" : "navigationStart",        # THIS PRESENTS NAVIGATION STARTIN
        "cle" : "domContentLoadedEventEnd",
        "lee" : "loadEventEnd",
        "fpt" : "firstPaint",
        "fcp" : "firstContentfulPaint",
        "trc" : "totalResource",
        "rlt" : "totalResourceLoadTime",
    }
}
