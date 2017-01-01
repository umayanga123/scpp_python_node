def attacker_succses_probability(M, N, A, T):
    total_system_miner = M;
    attack_miner_count = A;
    verified_miner = N
    remain_miner = M - (A + N)
    normal_one_protocol_pin_timing = T;
    waiting_time_period = 45

    current_tranaction_propability = (float(N) / M);
    verification_lavel = 0.75;

    if (A < 3):
        if (current_tranaction_propability >= verification_lavel):
            print "Transaction Verified (Current Verification Level ) : %s" % current_tranaction_propability;
        else:
            print "Transaction Not Verified (Current Verification Level )  :%s" % current_tranaction_propability;
            remaining_time_to_verified = 45 - (3 + (M * 1) + (N * 1));
            print "Remain Time to Verified : ", remaining_time_to_verified ,"s"
            T = round(T, 0)
            hops = 0;
            print "Approximate Time hope (Time for One Ping) ", T ,"s"
            for x in range(1, remaining_time_to_verified + 1, int(T)):
                if(x +remaining_time_to_verified <= 45):
                    tranaction_sucusses_proper = float(x) / remaining_time_to_verified;
                    print  "Time :   %s s Transaction Successes Probability(According to Remaining Time): " % (x + remaining_time_to_verified), (
                        1 - tranaction_sucusses_proper)
                    hops += 1;
            print "Attacker Successes minimum  probability(Accoding to Remaing Pins :" , float(1)/hops

    else:
        print "Transaction Not Verified Attacker Success : %s" % current_tranaction_propability;


##M -Total Miners count,  N - Transaction Verified Miners count ,A-Attacker Count , T - Time
print "Have to receive one miner Response"
attacker_succses_probability(10, 7, 2, 1.4);

print "\nHave to receive Two  miner Response"
attacker_succses_probability(10, 6, 2, 2);

print "\nHave to receive Two  miner Response"
attacker_succses_probability(10, 5, 2, 2);

print "\nTrust Network Success"
attacker_succses_probability(10, 8, 2, 1.4);

print "\nAttacker Success"
attacker_succses_probability(10, 7, 4, 2);

