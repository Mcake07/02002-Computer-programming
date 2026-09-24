current_record = 5.21
new_record_attempt = 5.42

if new_record_attempt > current_record :
    print(f"NY REKORD PÅ {new_record_attempt} OG SLOG DEN FORHÅNDVÆRENDE REKORD PÅ {current_record}!")
    current_record = new_record_attempt

else :
    print(f"Du slog ikke rekorden på {current_record} da du kun fik {new_record_attempt} ):")