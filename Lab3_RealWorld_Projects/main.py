import access_control

CONTROL_NUM = 4
FAVORITE_ARTIST = "FRANK OCEAN"
threshold = CONTROL_NUM * 5 # 20

@access_control.audit_log
def run_auth():
    level = access_control.compute_access_level(CONTROL_NUM, len(FAVORITE_ARTIST))
    decision = access_control.validate_access(level, threshold)
    return level, decision

# Result: Level = (4*3)+11 = 23; 23 >= 20 -> GRANTED
