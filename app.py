import cv2
import pyzbar
import time

import mysql.connector as mysql
from pyzbar import pyzbar

connection = mysql.connect(host="localhost",
                     user="root",
                     passwd="Modi123@",
                     db="inventory")
barcode_text = ""
def read_barcodes(frame):
    global barcode_text
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(type(barcode_text))
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame, barcode_text

def main():
    global barcode_text
    capture_duration = 30
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    start_time = time.time()
    while ret:
        ret, frame = camera.read()
        frame, barcode_text = read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if len(barcode_text) > 0:
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break




    camera.release()
    cv2.destroyAllWindows()
    return barcode_text


if __name__ == '__main__':
    # barcode_text = "sdfd"
    barcode_text = main()
    # print("here",barcode_text)
    # name = 'Bai Antioxidant Infusion'
    # mySql_insert_query = "INSERT INTO pantry (item_barcode,item_name) VALUES (%s, %s)"
    # values = (barcode_text, name)
    # mySql_insert_query = "INSERT INTO pantry (item_barcode,item_name) VALUES ({}, {});".format(barcode_text, name)
    cursor = connection.cursor()
    print(mySql_insert_query)
    ## executing the query with values
    cursor.execute(mySql_insert_query, values)
    connection.commit()

    print(cursor.rowcount, "record inserted")
