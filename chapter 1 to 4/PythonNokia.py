menu = """
   
    		Your 
       		   NOKIA 
          	       Menu 
                          map

		Enter-> 

      			1-> Phone Book 
      			2-> Messages
      			3-> Chat
      			4-> Call register
     		 	5-> Tone
      			6-> Settings 
      			7-> Call divert
      			8-> Games
      			9-> Calculator
      			10-> Reminder
      			11-> Clock
      			12-> Profile
      			13-> SIM servives
			"""
print(menu)
menu_map = int(input("Enter a number:\n"))
match menu_map:
	case 1:
		phone_book_menu = """
        			PHONEBOOK
  
  			Enter-->
				1-> Search
				2-> Service Nos.
				3-> Add name
				4-> Erase
				5-> Edit
				6-> Assign tone
				7-> Send b'card
				8-> Option
				9-> Speed dials
				10-> Voice tags
		
				"""
		print(phone_book_menu)
		phone_book = int(input("Enter a number:\n"))
		match phone_book:
				case 1: 
	      	 			print("Search")
				case 2:
	      				print("Service Nos.")
				case 3:
	      				print("Add name")
				case 4: 
	      				print("Erasing")
				case 5:
	      				print("Edit")
				case 6:
	      				print("Assign tone")
				case 7:
	     				print("Sending b'card")
				case 9:  
					print("Speed dial")
				case 10:
					print("Voice tags")
				case 8:		
				
		 			print("""
               							OPTION
  						Enter-->
          						1-> Type of view
	 		 				2-> Memory status

         
								""")
		
		option_number = int(input("Enter a numb:\n"))

		match option_number:
							case 1: 
								print("Types of view")
							case 2:
								print("Memory status") 
				  
							case _: 
								print("invalid")		
				
	case 2:
		print("""
             					MESSAGE
  					Enter-->
         					1-> Write message
		 				2-> Inbox
	 					3-> Outbox
	 					4-> Picture
	 					5-> Template
	 					6-> Smileys
	 					7-> Message settings
	 					8-> info service
	 					9-> Voice mailbox number
	 					10-> Service command editor
						""")
		message_number = int(input("Enter a number:\n"))
		match message_number:
					case 1: 
						print("Write a message")
					case 2:
						print("Inbox")
					case 3: 
						print("OutBox")
					case 4: 
						print("Picture messages")
					case 5: 
						print("Templates")
					case 6: 
						print("Smileys")
					case 8:
						print("Info services")
					case 9:
						print("Voice mailbox number")
					case 10:
						print("Service command editor")
					case 7: 
						print("""
						
							1-> Set
							2-> Common
							""")
		messages_input = int(input("Enter a number"))
		match messages_input :
			case 1:
				print("""
 						        		SET				
					         		Enter-> 
									1-> Message center number
									2-> Messages sent as
									3-> Message validity
										""")
		
				set_input = int(input("Enter a number"))
				match set_input: 
					case 1:
						print("Message center number")
					case 2:
						print("Messages sent as")
					case 3: 
						print("Message validity")
 												
			case 2:
				print("""
									COMMON
						  		Enter-->  
									1-> Delivery
									2-> Reply via same center
									3-> Character support
										""")
		
				common_input = int(input("Enter a number"))										
				match common_input: 
						case 1: 
							print("Delivery")
						case 2: 
							print("Reply via same center")
						case 3:
							print("Character support")
										
     
	case 3: 
		print("Chat")
						
	case 4: 
		print("""
		CALL REGISTER
	Enter-->
		1-> Missed calls 
		2-> Recieved calls
		3-> Dialled numbers
		4-> Erase recent call list
		5-> Show call duration
		6-> Show call cost
		7-> Call cost settings
		8-> Prepaid credit
		""")
		call_register_prompt = 	int(input("Enter a number"))
		match call_register_prompt:
						case 1: 
							print("Missed calls")
						case 2:
							print("Recieved calls")
						case 3:
							print("Dialled numbers")
						case 4:
							print("Erase recent call list")
						case 5: 
							print("""
							Enter--> 
								1-> Last call duration
								2-> All call duration
								3-> Recieved calls duration
								4-> Dialled calls duration
								5-> Clear timers
									""")
							call_duration = int(input("Enter a number"))
							match call_duration:
											case 1:
												print("last call duration")
											case 2:
												print("All call duration")
											case 3:
												print("Recieved calls duration")
											case 4:
												print("Dialled call duration")
											case 5: 
												print("clear timers")
						case 6: 
							print("""
							    SHOW CALL COST 
						Enter-->
							1-> Last call cost
							2-> All calls' cost
							3-> Clear counters
								""")
							call_cost = int(input("Enter a number"))
							match call_cost:
									case 1: 
										print("Last call cost")
									case 2:
										print("All calls' cost")
									case 3:
										print("Clear counters")
						case 7:   	
							print("""
								CALL COST SETTINGS
							Enter-->
								1-> Call cost limit
								2-> Show cost in
								""")
							call_settings = int(input("Enter a number"))
							match call_settings:
										case 1:
											print("Call cost limit")
										case 2:
											print("Show cost in")
		
	case 5:
		print("""
		TONE
  	 Enter-->
	1-> Ringing tone
	2-> Ringing volume
	3-> Incoming call alert 
	4-> Composer 
	5-> Message alert tone
	6-> Keypad tone
	7-> Warning and game tones
	8-> Vibration alert
	9-> Screen saver
	""")
		tone_prompt = int(input("Enter a number"))
		match tone_prompt:
				case 1:
					print("Ringing tone")
				case 2:
					print("Ringing volume")
				case 3:
					print("Incoming call alert")
				case 4: 
					print("Composer")
				case 5: 
					print("Messages alert tone")
				case 6:
					print("Keypad tone")
				case 7: 
					print("Warning and game tones")
				case 8:
					print("Vibration alart")
				case 9: 
					print("Screen saver")
	case 6: 
		print("""
			Settings
		Enter--> 
			1-> Call settings
`			2-> Phone settings
			3-> Securitybsetting
			4-> Restore factory settings
				""")
		call_settings = int(input("Enter a number"))
		match call_settings:
						case 1:
							print("""
								CALL SETTINGS
							Enter-->
							1-> Automatic redial
							2-> Cell info display
							3-> Call waiting option
							4-> Own number sending 
							5-> Phone line in use
							6-> Automatic answer
								""")
							callsettings = int(input("Enter a number"))
							match callsettings:
									case 1:
										print("Automatic redial")
									case 2:
										print("Call waiting option")
									case 3: 
										print("Call waiting option")
									case 4: 
										print("Own number sending")
									case 5: 
										print("Phone line in use")
									case 6:
										print("Automatic answer")
											
						case 2:
							print("""
							LANGUAGE
							Enter-->
							1-> Language
							2-> Cell info display
							3-> Welcome note
							4-> Network selection
							5-> Lights
							6-> Confirm SIM service actions
							""")

							language = int(input("Enter a number"))
							match language:
								case 1:
									print("Language")
								case 2:
									print("Cell waiting option")
								case 3:
									print("Welcome note")
								case 4:
									print("Network selection")
								case 5:
									print("Lights")
								case 6:
									print("Confirm SIM services actions")
						case 3:
							print("""
							SECURITY SETTINGS
							Enter-->
							1-> PIN code request
							2-> cell barring service
							3-> Fixed dialling 
							4-> Closed user group
							5-> Phone security
							6-> Change access codes
								""")
							security_settings = int(input("Enter a number"))
							match security_settings:
										case 1:
											print("PIN code request")
										case 2:
											print("Cell barring services")
										case 3:
											print("Fixed dialling")
										case 4:
											print("Close user group")
										case 5:
											print("Phone security")
										case 6:
											print("Change access codes")
												
						case 4:                                                     
							print("Restore factory settings")
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		print("""
			CLOCK
		Enter-->
			1-> Alarm clock
			2-> Clock settings
			3-> Date settings
			4-> StopWatch
			5-> Countdown timer
			6-> Auto update of date and time
				""")
		clock = int(input("Enter a number"))	
		match clock:
				case 1:
					print("Alarm clock")
				case 2:
					print("Clock settings")
				case 3:
					print("Date settings")
				case 4:
					print("Stopwatch")
				case 5:
					print("Countdown timer")
				case 6: 
					print("Auto update of date and time")
	case 12:
		print("profile")
	case 13:
		print("SIM services")
	case _:
		print("Invalid")
		
						

		
	              												
 							