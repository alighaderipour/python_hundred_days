def processing_items(item_type, **kwargs):
    print(f"processing {item_type} : ...")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("processing done")


processing_items(
    "book", title="100 Years Solitude", Author="Gabriel GarciaMarquez", price="43$"
)
processing_items(
    "book", title="Crime and Punishment", Author="Dastaiovski", price="41$"
)
processing_items("Ball", size="medium", sport="Voleyball", price="21$")
