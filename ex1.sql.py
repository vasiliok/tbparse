SELECT 
TIPP_ID ID, 
TIPP_FILENAME FILENAME, 
TIPP_ART ART, 
DECODE(USERT_TIPP_ID, USERT_TIPP_ID, 'J', 'N') GELESEN

FROM 
W_TIPP@ETK_NUTZER     
LEFT JOIN W_USER_TIPPS@ETK_NUTZER ON (USERT_FIRMA_ID = '111'  AND USERT_ID ='ADMIN' AND USERT_TIPP_ID = TIPP_ID) 
WHERE TIPP_ID > 0 AND TIPP_WICHTIG = 'N' 
ORDER BY TIPP_POS