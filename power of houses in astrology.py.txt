import os
from kerykeion import NatalAspects, KrInstance, print_all_data
import math
from datetime import datetime, timedelta
import time

planets=["Uranus","Saturn","Jupiter","Mars","Sun","Venus","Mercury","Moon"]
aspect_names=["quincunx"]

sign_ascending_no_planet = [
    "    This sign ascending at birth produces a person of small stature, lean body (unless it be in the first part of this sign, which would then make it more fleshy), strong, large bones and limbs; a swarthy or sallow complexion, with sandy or light coloured hair and piercing eyes. The disposition is determined and impulsive. The nature of this sign inclines the native to anger, but makes him witty, ingenious and of quick perception. Saturn or Mars therein would alter it for the worse, whereas the effect of Jupiter or Venus would be for the better. \n    Should a sign be strongly occupied by planets, these would entirely change its nature and effects; otherwise each sign would unalterably follow its own nature.\n    Mars is the ruler or significator of the Aries person.",
    "    Signifies a person of short, thick-set stature; full face, dark curling hair and swarthy complexion. The disposition would be somewhat unfeeling, impulsive, self-assertive, confident, injudicious, slow to anger, but when roused, violent and furious as a bull and difficult to appease; swayed by passions, likes and dislikes. It is the sign of self-appreciation, and Venus is the ruler or significator thereof.",
    "    The person defined by this sign would be tall and straight, with long arms but short hands and feet; rather dark complexion, with a bright and lively expression in fine eyes of a dark hazel colour. This sign gives good mental attributes, excellent understanding and a great fluency of speech; it makes the native judicious in worldly affairs, temperate, receptive in mind, highly intuitive, and very unlikely to go to extremes in anything. They are children of moderation. Mercury is the ruler or significator.",
    "Indicates a person of small or short stature, the upper part of the body being generally larger than the lower. The face is round, with a pale, sickly complexion, brown hair, grey eyes. The Cancer person is mild, gentle and sympathetic; the Moon is the ruler or significator. The disposition would be unstable and inconstant, timid, and void of energy. The constitution weak and effeminate; if a woman, she may have many children.",
    "    This is a regal, commanding and eastern sign; the only house of the Sun, and as such is by nature hot, dry, fiery, masculine and barren. The native of this kingly sign is generally of a good full stature with broad square shoulders.\n One of the characteristics of the Lion is an austere countenance, with large, commanding eyes, a fearless and sprightly glance which becomes fierce under provocation; the face is oval and complexion ruddy or sanguine, with dark or yellow flaxen hair. The disposition is open, bold, courteous, firm, ambitious, and quick in judgment; the heart generous, the mind aspiring and lofty with a resolute and courageous spirit. The Sun is the ruler or significator.",
    "This sign in the ascendant gives the native a stature somewhat above medium height with a well-formed, slender body; a round face, complexion ruddy brown, with lank hair of a black or dark brown colour; the voice is thin and shrill. The disposition is studious but lacking in firmness, the mind witty and ingenious.\n    Should this sign ascend with Mercury therein, free from the malevolent aspect of Saturn and the Moon in Cancer, the native would make an excellent orator. Mercury is ruler or significator.",
    "    Produces a tall, well-made body; round and lovely face with a fine sanguine complexion and grey eyes; the hair long and lank of a yellow or flaxen colour. In old age the face will be full of pimples or of a deep red colour. In disposition, friendly and affable. Though with self-esteem the mind will be just and upright, amiable, with conversible power and independence of character; specially intuitive. Venus is ruler or significator.",
    "    Prefigures a strong, robust and corpulent body of middle stature, with short neck and legs; a broad face, brown complexion and brown curling hair; secretive and not to be trusted--capable of dissimulation; these people are never straightforward. The subject will be reserved and thoughtful in conversation, but deceitful; a veritable Talleyrand, unfeeling, and often abrupt; unrefined, inelegant, coarse, without any sympathy, if Mars has an evil aspect to Mercury. Mars is ruler or significator",
    "This sign rising in a natus endows the native witha well-formed, strong, and active body, somewhat above the middle height; face rather long, handsome and comely; ruddy complexion and chestnut hair. Such a person generally makes a good horseman; is intrepid, courageous and careless of danger. He is generous, free and good-hearted, with regard for honour and rectitude. Jupiter is the ruler or significator.",
    "    The house of Saturn and the exaltation of Mars is a four-footed sign and of the earthy triplicity. It is a cold, dry, melancholy, feminine, noncturnal, movable, cardinal, domestic and southern sign. Persons born under this sign are of a slender stature and not very well-formed, with long, thin face and neck, dark-hair, narrow chest and thin beard. The disposition is sharp, witty and subtle; selfish and covetous; often sensitive and nervous. They are capricious and impressionable. Saturn is the ruler or significator.",
    "    This is the house of Saturn and of the airy triplicity. It makes a well-set, stout and robust person witha a somewhat long, pale and delicate countenance; clear complexion, bright sandy or dark flaxen hair. The disposition is kind-hearted; a gentle and even temper, witha scientific turn of significator. Some modern writers say that Uranus is the ruler or significator.",
    "    The twelfthsign is of the watery triplicity. It is a cold, moist, feminine, phlegmatic, common and fruitful. It is the house of Jupiter, and in it Venus is exalted. The native would be of a short, thick stature, round shouldered; with pale complexion and brown hair. The nature of the sign does not tend to a robust temperament. It gives a lazy and slothful disposition, inactive, easiful, and lacking the energetic principles and physical activity. The physical condition is often a clog to mental action. They lack the self-assertive and aggressive power and are too easy-going. Jupiter is ruler or significator."]
planets_on_ascendant = [[
                            "Defines a well-formed stature, medium height, rather slender, sanguine complexion, fair hair; the disposition fitful, changeable, ambitious, very impressionable, with much self-esteem.",
                            "Short stature, rather corpulent, pale complexion, darkish hair; and unrefined nature, obstinate, boastful, and malicious.",
                            "Moderately tall figure, well-built, fair complexion, light-brown hair; ingenious, ambitious and subtle in disposition; intuitive, generally clever and fond of scientific subjects.",
                            "Low stature, sanguine complexion, darkish brown hair; quick to take offence, but soon forgives; wayward, impulsive, rather fond of drink, lacking tenacity of purpose.",
                            "Middle stature, light brown hair, fair complexion; possessing self-importance, exaggerated pride; a little stubborn and arrogant.",
                            "Medium height, fairly well built, thin body, brown hair; the native will be ingenious, with a taste for sciences and literature; eccentric, impressionable, miserly and malicious. We have observed that such people are quick at learning, quiet, reserved, adopting a line of their own, and fond of searching for curiousities; hasty tempered, taking no notice of others and never led by them.",
                            "A tall, well-made person, fair hair, pale complexion; this is a person of great precision and will-power, aspiring, proud, sensitive and fond of sciences; if aspected by Venus and Mercury, Uranus gives good abilities.",
                            "Medium height, well-built person, dark complexion and hair; a most undesirable acquaintance, malicious, crafty, unreliable, fond of drink, sometimes most dangerously agressive if provoked.",
                            "Well-made person, fair complexion and hair; candid and generous, energetic, fond of recreations; a man often swayed by impulse",
                            "A small darkish person, not well formed, dark or pale complexion, dark brown hair; selfish, vindictive, fickle and malicious; with great ideas of his own abilities.",
                            "A person of medium stature, fair complexion. brown hair; impressionable, studious, penetrating, eccentric, prudent, intelligent, and often fond of studying sciences.",
                            "Short, not well-formed stature, palish complexion, brown hair; often cast down and indulgent, not intellectual; easy going and pleasure loving; a man of little wit."],
                        [
                            "Medium height, lean and well made, ruddy complexion, high forehead, large, full eyes, dark hair, little beard; in character this person will be ill-natured, quarrelsome, bossful, self-conceited, cruel and revengeful if crossed in his purposes.",
                            "Indicates one of small stature, lean, ill-made, dark hair. He is generally inclined to be vicious, revengeful and given to all sorts of dissipations. The most ignoble of men is the Saturn in Taurus person and treacherous; he is a cowardly fellow, untrustworthy; one who vows vengeance and would stab in the dark.",
                            "Rather above the middle height with a well proportioned body; the face oval, hair either black or dark brown; of an ingenious and humane nature, somewhat perverse, unfathomable and subtle, generally unfortunate.",
                            "Signifies one of medium height, thin, and sometimes crooked or ill-made; the constitution sickly, the face thin with brownish hair; in his behaviour he will be deceitful and malicious, of a cunning nature, and much given to drink and vicious actions; heavy and dull.",
                            "A somewhat noble bearing of middle stature, broad shoulders and large bones, the hair a light brown; the temper would be passionate and malicious; the person given to boasting; but lacking in courage, and really not so noble and bold as he looks; the courage is more apparent than real.",
                            "A tall and spare body, swarthy complexion, black or brown hair; this person would be rather melancholy, fond of learning, malicious, inclined to be dishonest, unforgiving, reserved and subtle.",
                            "Represents a tall person with a handsome and well-formed body, oval face, broad brow and brown hair; high spirited, self-conceited, antagonistic, selfish, fond of argument and soon moved to anger, independent, proud and opinionated.",
                            "A short stature, thick set, black or brown hair; arrogant, quarrelsome, apt to be mean and base in his actions, in fact, a mischief maker of the worst kind; if Mars is in evil aspect to Saturn, hi is a wicked man.",
                            "Handsome, well formed person of middle stature, with brown hair; in his behaviour, courteous to all (though rather irascible and hasty), obliging and forgiving.",
                            "A rather lean person of medium height, long face, sallow complexion, black or brown hair; he is avaricious, melancholy, grave, discontented, peevish, not easily pacified in anger; most revengeful and double-faced if Saturn has the cross aspects of Mars.",
                            "Denotes a person of middle stature, rather inclined to be stout, black or brown hair; a lover of arts and sciences, of a courteous disposition, but very conceited; a person of much ingenuity and sometimes of genius; prodent and shrewd.",
                            "Middle stature, pale complexion, and black or dark brown hair; most malicious, contentious, sottish person; deceitful in his dealings; deliberate and yet fickle in his actions; antagonistic, severe and untrustworthy."],
                        [
                            "Produces one of middle stature, oval visage, ruddy complexion, brown or flaxen coloured hair, with sharp sight; an obliging person of free and noble disposition, a lover of friendship and peace; if near violent and fixed stars it renders the person rash and fickle.",
                            "Medium height, swarthy complexion, brown hair; wise, discreet, humane, kind-hearted and sympathetic; of a good carriage and a lover of the fair sex.",
                            "A well-formed, tall body above the middle height, sanguine complexion, brown hair; a lover of arts and science, delighting in ladies' society, courteous, frank and obliging.",
                            "Of medium stature, oval face, pale complexion, dark brown or black hair; thoughts somewhat aspiring, aiming at great things; a busybody, conceited, but well-disposed; a great lover of the other sex.",
                            "Portrays one of a tall stature and a well-proportioned body, light coloured or yellow curling hair, ruddy complexion; of a good disposition, just generous, free and courteous, delighting in manly and heroic actions, courageous, desirous of honour, and quick to resent an injustice.",
                            "Generally a handsome, well-composed person, brown or black hair; he is ambitious, covetous, boastful, a lover of money, of a hasty disposition and certainly not generous; much given to the study of arts and sciences.",
                            "Designates a tall, well-made person, oval and pleasant countenance, light brown or flaxen hair; the disposition is very good, delighting in all pleasant recreations, free, generous and obliging; a most attractive person.",
                            "Medium stature, compact, well-built body, brownish hair; the native is conceited, ill-natured, covetous, arrogant, ambitious and industrious.",
                            "A tall, upright, well-formed body, oval face, ruddy complexion, hair of a chestnut colour; in disposition just, noble, perfectly trustworthy, with the strongest internal consciousness of right and duty; a lover of horses and a good horseman.",
                            "Short stature, think face, pale complexion, brown hair; this person wold be delicate in constitution, peevish, desponding and ill-natured (if Jupiter is afflicted), of a mutable nature and inconstant in attachments; if Jupiter is well aspected, the disposition is good.",
                            "Denotes a person of well-set, middle stature, good complexion, brown hair; a pleasant, merry dispositon, delighting in good company, just, merciful and of an amiable nature; a great favourite and always much appreciated; personality attractive.",
                            "A mean stature, inclined to stoutness, light brown hair; studious, good-hearted and very ingenious, a lover of mirth and music, constant in attachment and affectionate; generally fortunate in travelling by water."],
                        [
                            "Indicates a well-set, big-boned person of middle stature, swarthy complexion, curling hair (sometimes red or of a light colour), hazel eyes, with a sharp, bold, confident glance; a bold, courageous, masterful disposition, fond of ruling and war; austere, quick in anger and combat, war-like and proud.",
                            "Medium stature, inclining to stoutness, dull complexion, broad face and features, black hair; this person has often a mark of some weapon on his face; he is treacherous, deceitful, frequently vicious and profligate; ill-natured. If Mars is near the Pleiades he is unfortunate.",
                            "Tall, well-proportioned person, black or brown hair; a wandering, unsettled mind; with an irascible, rash and turbulent nature; ingenious, but not fortunate.",
                            "Short, not well-proportioned stature; in fact, often deformed; dull, white complexion, brown hair; this native will be of a sottish and oppressive disposition; fond of drink and quarrelsome, bad tempered and servile, ignoble, capable of meanness, unfortunate through his own actions, often unmannerly and rude.",
                            "Portrays a tall, well-made body, endued with health and strength; big face, large eyes, dark, flaxen-coloured hair; the disposition hasty, choleric, generous, noble, and fond of out-door sports; very firm, but not ill-disposed. He will vaunt and is a lover of warlike pursuits.",
                            "A well-proportioned stature of medium height, swarthy complexion, brown or black hair, hasty in anger, unforgiving and irritable; the native will be revengeful, cenceited, hard to please and unfortunate in his undertakings. The student should also notice if Mars is well aspected by Jupiter, Sun, or Moon, as this would considerably alter the significations for the better.",
                            "A rather tall, well-made body, oval face, cheerfyl and pelasant expression, sanguine complexion, light brown hair; this person will be ambitious, quick in anger, conceited and boastful, amiable, fond of dress and cheerful.",
                            "Well-set person of medium height, swarthy complexion, broad face, black curling hair; clever in arts and sciences, of good abilities, but of an ungrateful, revengeful, cruel, quarrelsome and deceitful disposition; a man of subtlety and penetration, he is clever but not good.",
                            "Denotes a tall, well-proportioned person, oval face, very good complexion, brown hair; in disposition hasty, but generous and free, delighting in warlike pursuits, fond of good and merry company; high-minded, jovial, courageous, loquacious, fond of approbation and of applause, a good disposition, and those who would propitiate him must applaud him.",
                            "Short, lean stature, thin face, small head, bad complexn; in mind very ingenious, quick-witted, courageous and high-minded, possessing, on the whole, a good disposition; the native is generally fortunate and happy in most of his undertakings, penetrating, with a deductive judgment, shrewd, and sees more of his environment than most people; he is discreet (unless Mars is afflicted) and has great determination--a contriver, of skilful capacity; men of ability and discernment have Mars rising in Capricorn.",
                            "Medium and well-proportioned height, good complexion, red or sandy-flaxen hair; quarrelsome, fond of argument (in which he will seldom get the best), of a turbulent nature, generous and quick to forgive, soon provoked and soon appeased; his want of prudence tends to ill-fortune.",
                            "Short, fleshy, badly composed stature, light brown or flaxen coloured hair, bad complexion; this is a deceitful person of a dull and stupid understanding, dissembling, indolent, artful, sottish, sensuous and untrustworthy--an uncertain quantitiy--a man of artifice and pretence, shifty and covert."],
                        [
                            "Denoes a strong, well-formed, middle stature, good complexion, light flaxen hair; in disposition lofty, noble and generous, even to his enemies, spirited and an independent character; he delights in war and generally gains honour and renown therein. If the Sun is in good aspect to Mars, the native is a man of valour and victory.",
                            "A short, well-set person, broad face, dull complexion, wide mouth, large nose, brown hair; he is proud, bold, self-confident, fond of strife, and hasa great idea of his own opinions with exaggerated self-importance.",
                            "Well-formed body, large stature, sanguine complexion, brown hair; this person does not easily take offence, and is of a courteous, affable disposition, even tempered, mild, kind hearted, and sometimes imposed upon by others through a too confiding, unsuspicious nature.",
                            "An unhealthy person of small stature, bad complexion, brown hair, sometimes with a defect in the face; he is a jovial and boon companion, delighting in all kinds of sports and pastimes, good natured, pleasant and generous, harmless, cheerful, lacking executive power, and fond of the other sex.",
                            "This planet in his own house gives a well-proportioned, strong body, full face, sanguine complexion, light or yellow hair, fine, large, expressive eyes; the native would be proud, noble, faithful, just, and true to his promises, disdaining mean or sordid actions; a lover of good and pleasant company, of commanding appearance; ambitious of honour, magnanimous, fond of authority, and easily susceptible to indignities.",
                            "A tall, well proportioned stature, rather slender, and abundance of brown or black hair, good complexion; a pleasant, ingenious, scientific person of good disposition though rather austere; cheerful, convival, fond of recreations.",
                            "Describles a person of upright and erect carriage, oval visage, good complexion, full eyes, light coloured hair; he is proud, extravagant, apt to be unfortunate and exposed to much danger, especially in war; he often falls short of his aspirations; the mind is honourable and the disposition good.",
                            "Square, well-set person of middle stature, dusky complexion, fleshy face, brown hair; of a rugged, ingenious nature, clever in war and on the sea, opinionative and antagonistic; ambitious, overbearing--a man of honest bluntness.",
                            "Represents a tall, well-set, comely person of sanguine complexion, oval face, light brown hair; the native will be high spirited, proud, ambitious of honour, lofty and noble in disposition, scorning to take a mean advantage, fond of sports; austere, aristocratic, a man who delights in philanthropy.",
                            "Small, ill-proportioned stature, thin, spare body, oval face, pale complexion, brown hair; just, witty, ingenious, of an undaunted spirit and fond of ladies' society; good natured, though often hasty, reasonable and good tempered.",
                            "A well-composed, corpulent body, of medium height, full, round face, good complexion, light brown hair; pround, ambitious, fond of ruling, but well-disposed; ostentatious, free from vindictiveness and rather vain; the disposition is good.",
                            "A person of low, stout stature, round face, pale complexion, light brown or flaxen hair; if a male, he will be a lover of the other sex, fond of sports, a spendthrift and prodigal; otherwise inoffensive, often effeminate, extravagant and intemperate; a man of indulgences."],
                        [
                            "Portrays a slender, fairly well-proportioned body, of middle stature, good complexion, light hair; as Venus is in her detriment in this sign, the person may be indiscreet in his acts; he will be of a restless nature and a lover of company, often pensive, mutable and uncertain, lacking tenacity.",
                            "A hnadsome, well-shaped person of medium height; the native is good-natured, obliging, a general favourite with everyone, fond of singing and dancing, humane, mild and even tempered, winning and kind-hearted.",
                            "Slender, well-made body, good complexion, brown hair; tender-hearted, honest and just in all his actions, kind to the poor, sympathetic and loved by all; mild, inoffensive and gentle.",
                            "Short, rather fleshy stature, round, pale face, light coloured hair; indolent, fickle and fond of drink, inconstant, often slothful and lacking energy.",
                            "Moderately tall person with a well-proportioned body, good complexion, round face (sometimes freckled), full eyes, light brown or sandy hair; in character-conceited, proud and passionate; but free, generous, forgiving, good-humoured, sociable, soon angry, but soon appeased.",
                            "Stature of medium height, well-formed body, dusky com plexion, oval visage, dark brown or black hair; an ingenious person of active, subtle mind, with an inquiring inclination after knowledge; eloquent, aspiring, with conversible power and seldom fortunate.",
                            "A well-proportioned, tall, upright figure, oval face (with dimples in the cheeks and sometimes freckles all over the face), sanguine complexion, pretty brown hair; the native is courteous, obliging, most amiable; a lover of good and virtuous company, generally well beloved by all.",
                            "Describes one of middle stature, well-set, rather fat, broad face, dark complexion, dark brown or black hair; & quarrelsome, envious and hateful person; often vicious, succumbing to temptations and unworthy actions, in short, a person of evil propensities.",
                            "Tall, well-made person, oval face, clear complexion, light brown hair; of great moral courage, noble spirit, free and generous in disposition, somewhat proud and passionate in anger, but soon over; fond of recreations, kind-hearted, good-tempered, an obliging, fortunate person, full of generous impulses.",
                            "Indicates a person of middle stature, spare body, thin face, pale and sickly complexion, dark brown or black hair; in character, conceited, fond of drink and a great boaster; often indiscreet, making rash changes to his detriment, greedy as to diet and fond of women.",
                            "Gives a handsome, well-proportioned body, very good complexion, light brown or flaxen coloured hair; very good disposition, courteous, obliging, a lover of peace, gentle, affable, and one who will eschew evil; humane, fortunate in his or her affairs, and much appreciated by friends.",
                            "A person of medium height, round face (and sometimes a dimple in the chin), good complexion, brown or flaxen coloured hair; of an ingenious wit, just in his dealings, a lover of peace and quietness; altogether a nice disposition; mild, good humoured, but lacking tenacity, which will make the native unstable."],
                        [
                            "Produces a short, thin, slender body, oval face, swarthy complexion, light brown hair; a discontented person, witty, clever, self assertive, impulsive, highly impressionable, ambitious, restless; an orator with conversible power.",
                            "One of middle stature, well-set, corpulent body, swarthy complexion, dark brown hair; fond of company and the other sex, lazy and loving his own ease, with a keen appreciation for good fare; self-indulgent, often indolent.",
                            "A well-made, tall person, good complexion, light brown hair; the native will be ingenious, intellectual, cultured, possessing great taste and a good mind for arts and sciences; a good disposition, quick, active and very clever.",
                            "Represents a person of short stature, thin face, bad complexion, sharp nose, small, expressionless eyes, dark brown hair; he will be malicious, fickle, given to stealing and lying; an uncertain quantity, with great finesse and a sharp tongue; a dissembler.",
                            "A large stature, swarthy complexion, round face, large eyes, light brown hair; a haughty, proud, mischief-making person of a contentious disposition; vaunting, lofty and choleric.",
                            "Tall, slender, well-made figure, long face, dark complexion, brown or black hair; fond of dress, ingenious, of a scientific and literary turn. of mind, subtle and careful of his affairs; well-disposed and generally accomplished person; Mercury unafflicted makes a good orator.",
                            "One of a moderately tall, well-composed stature, sanguine complexion, light brown hair; this person will possess a good disposition, be thrifty, ingenions, just, virtuous; fond of learning and all scientific subjects; an equitable person.",
                            "A middle stature, well-set, strong and able body, dusky com plexion, dark brown curling hair; this is a wit with few good qualities, fond of company and women; malicious, selfish, subtle, ill-disposed; he has an eye to 'number one.'",
                            "Rather tall, well-made, ruddy complexion, oval face, large nose, brown hair; quarrelsome, contentious, and, indeed, his own and worst enemy; the learning in this case is often mere pretence; his passion is soon appeased, he in hasty in judgment to his detriment.",
                            "A person of short stature (sometimes bow-legged), thin face, muddy complexion, light brown hair; often sickly; of a peevish and fickle disposition, sharp, active, acute and penetrating, easily perturbed, often complaining.",
                            "An indifferent stature, corpulent, fleshy body, full face, good complexion, brown hair; the native is of a scientific turn of mind, of great wit, often interested in occult subjects, very ingenious; a student, open-minded and sociable; usually beloved by his friends; with that intellectual ability which accomplishes much.",
                            "Low stature, sickly, pale complexion, thin face, brown hair; a drunkard, sometimes wasteful, indolent and peevish, often disconsolate, ambitious of honour."],
                        [
                            "Describes a person of well-made, medium height; round face, good complexion, light brown hair; in temper changeable, churlish and choleric, versatile, restless, mutable and often passionate; ambitious of honour.",
                            "A well-set, strong, corpulent body, middle stature, black or dark brown hair; the disposition is sober, obliging, gentle and just; the person is much liked, being very amiable, attractive in personality, and good tempered.",
                            "One of tall, well-proportioned stature, good complexion, dark brown hair; this is a deceitful, crafty, ill-natured, subtle person of a very ingenious mind.",
                            "Well-proportioned, rather fleshy, middle stature, pale complexion, round face, dark brown or black hair; a pleasing and kind disposition, just and wise, good-natured and candid; the native is indulgent, inoffensive, rather lacking in resolution, versatile, but singularly free from passion.",
                            "This seldom proves a fortunate person. The stature is large, body well-made, full face, large eyes and light brown hair; the person will be proud, ambitious, domineering, of lofty airs, consequential, hating to be under subjection to anyone and beloved by few; a man of self-importance.",
                            "Portrays a person of large stature, indifferent complexion, long face, black or dark brown hair; a pensive and ingenious nature; but covetous, imposing, miserly, selfish, loquacious, often melancholy and seldom fortunate.",
                            "Moderately tall and well-made person, sanguine complexion, light brown hair; a nice disposition, very amiable, fond of music, dancing, and all recreations; much appreciated by the other sex, eminently fitted for social functions.",
                            "A short, and often fat, person, pale, dark complexion, black or dark brown hair; malicious, treacherous and covetous in disposition, conceited, ill-conditioned or ignoble; such people gain little love from their neighbours and have a great liking for drinks.",
                            "Well-formed, middle stature, sanguine complexion, oval face, light brown hair; in temper, hasty but forgiving; a passionate, ambitious, but obliging person, lacking tenacity of purpose, free-spirited, aiming at great things.",
                            "Low stature, body and face spare and lean (often with some defects in the knees), brown or black hair; the native will be selfish, idle, indulgent, and indeed have few good qualities; a servile creature, mean and often sensuous.",
                            "Defines a middle stature with a well-made, rather corpulent body, sanguine complexion, brown hair; this person has an inventive nature, and is of a courteous, ingenious and good disposition; the personality is attractive; delighting in recreations, and abhorring low and evil deeds.",
                            "Short, rather obese stature, pale complexion, bright brown hair; an indolent, sottish person, easy going, with some sensuousness, and susceptible to gaming and drinking."]]
planets_on_houses = [[
                         "Changes in monetary affairs. If afflicting either of luminaries, heavy losses and bankruptcy may be the result; in any case, mutations of fortune.",
                         "Many changes and much unsettledness, especially if aspected by the Moon. The influence of Uranus in this house, especially on the mind, is great, and, if aspected by Mercury, gives good abilities. In fact, the planet has a peculiar influence on all things connected with this house, such as letters, writings, neighbours, and relations. It also inclines to the occult studies.",
                         "Disagreements with parents; trouble with property or inherit ance, and, unless well-aspected, misfortunes in life's eventide.",
                         "No offspring, if in barren signs; loss in gaming or speculating; if aspected by the Moon or Venus, too much given to dissipation, which often brings disgrace.\n This position is never good for the attainment of a high moral character. Uranus in this house, afflicting the Moon, produces sensuality in the nativity of a male.",
                         "Troubles from servants, and, if afflicting the Sun or Moon, some peculiar disease is to be feared.",
                         "An unhappy marriage, if any. This is bad for public undertakings, partnerships, and dealings with lawyers. The position delays marriage.",
                         "If ill-aspected, a marriage partner poor in worldly troubles with legacies, and, if afflicted, the native loses them. Subsequent evil aspects of the Sun to Uranus often cause early death, if within orb of the aspect at birth.",
                         "If aspected by Mercury, the native will be clever; if by the luminaries, he will have changes. The planet in this house influences the mind greatly expect evil in all things connected with this house, if Uranus be badly aspected.",
                         "Mutations in honour, credit, esteem, and employment; troubles with superiors, employers, and changes in the vocation; often sudden losses in business, if afflicting the Sun.",
                         "Inconstant friends, and if afflicted, they may ruin the native by a pretended friendship. If well-aspected, help from friends.",
                         "Secret enemies and jealousy."], [
                         "Troubles in all monetary matters, and especially so when afflicted by the luminaries. If well-dignified and unafflicted, success with landed property, income therefrom.",
                         "Misfortune in travelling, or through neighbours, brethren and relatives, with letters and writings. If he aspect the Moon or Mercury the native will be suspicious, stubborn, jealous and cautious to excess.",
                         "If afflicted, the father suffers in health and survives not many. years. If undignified or ill-aspected, a miserable and poor eventide of life. If well-aspected or dignified, the contrary; the native will probably inherit and have lands and property bringing him in gold, which he will carefully board.",
                         "This position is bad for speculation and sports of any kind. If ill-aspected, sickness or death of offspring, but especially when he afflicts the luminaries.",
                         "Bad servants, losses through them and much sickness, especially if in bad aspect to the luminaries; in common signs, weak chest and lungs; in cardinal signs, chronic indigestion and disordered system; in fixed signs, bladder troubles, heart disease or syncope, and often chronic rheumatism.",
                         "A selfish, cold, melancholy, reserved marriage partner; bad for partnerships, lawsuits and public dealings; more so if afflicting the Sun or Moon. The wife or husband delicate in health, and the marriage seldom proves a happy one; it delays or prevents marriage.",
                         "Probably a partner of little substance; trouble with legacies and wills. If well-aspected and well-dignified, the trouble will be mitigated, and there might even be gain in these matters; the partner might then possess money.",
                         "He strongly influences the mind, making the native more or less fearful, cautious, reserved, with inclination for religious beliefs; if afflicting the luminaries, unfortunate and dangerous long journeys, great suspicion, taciturnity and maliciousness when afflicting the Moon; particularly if the latter is in the ascendant, it often causes strange dreams and visions.",
                         "If dignified and well-aspected, some success in business; when ill-aspected, disgrace, losses and trouble. If afflicting the Moon, sickness and ill-fortune to the mother.",
                         "False friends, unless well-aspected; if ill-aspected, injury from them.",
                         "Many secret enemies, and if ill-aspected, the native will suffer through them; he has to fear false accusations and imprisonment."],
                     [
                         "Prosperity and success in wealth, especially if the planet is strong and essentially dignified, and well-aspected; if afflicted, little gain, and money difficulties.",
                         "Successful journeys; help from relations and neighbours. This position adds benevolence of mind, and kindness.",
                         "Unless much afflicted and ill-dignified, this shows success in life, especially towards the end, and the father in a good position with possessions. The native often acquires property; but evil aspects to Jupiter would indiente the contrary.",
                         "Model children, who will rise in the world. This position is good for gaming, sports and speculations, pleasure in life; if Jupiter is ill-aspected, the contrary.",
                         "Good health and faithful servants; benefits from the lower classes. If ill-aspected by the Sun, corrupted blood and deranged liver; in the common signs, trouble with the lungs; in the cardinal signs, deranged stomach and system.",
                         "A successful and happy marriage; favourable for partnerships and lawsuits; success as a lawyer. The native gets a good marriage partner; if afflicted, the reverse of all this.",
                         "Money by marriage and by will, unless badly afflicted.",
                         "A sincere, religious person, of high moral character. For tunate long journeys, either by sea or land; success in science, art, and publishing: should Jupiter be badly aspected, it would counteract all this.",
                         "Success in business; honour and esteem; a happy mother; success in life. Jupiter in this house, in good aspect to the luminaries, vouchsafes pence and prosperity; if in cross aspects, there would be little pence and prosperity.",
                         "Many faithful and valuable friends; realisation of hopes and desires; if in cross aspects, the reverse.",
                         "The native will have great power of attraction, and be successful in dealings with large cattle; but not so, if Jupiter is afflicted."],
                     [
                         "Great generosity; the native squanders his money and is lavish. May embarrass his fortune through rash actions in business and things speculative.",
                         "Stubborn, perverse and headstrong; danger in travelling; if afflicted, quarrels with and losses through brethren and neighbours, troubles through writings or short journeys.",
                         "Troubles with the home and the father. Bad for the eventide of life, if Mars be afflicted. In Aries or Capricorn and well-aspected, this planet vouchsafes some of this world's goods.",
                         "Trouble with offspring; if afflicting the luminaries, they will die early and suddenly either by accident or otherwise; fondness for gambling and speculation, causing great loss; very unfortunate in a lady's horoscope; often too fond of pleasure and dissipation. afflicted by 3 in this house would cause the native to form a liaison.",
                         "Bad servants. In the common signs, liability to chest troubles; if ill-aspected by the Sun or Moon, liability to inflammatory distempers; in the fixed signs, bladder troubles, disease of the heart or throat in the cardinal signs, headache, indigestion, acute rheumatism.",
                         "An unfavourable marriage; quarrels with the husband or wife, and if much afflicted, probable separation; ill-luck attends partnerships. It delays or prevents marriage in a female's horoscope. Begets many open enemies.",
                         "A lavish or wasteful marriage partner; quarrels through legacies, wills, and the marriage partner's pecuniary affairs.",
                         "Extremely obstinate and despotic, suspicious and critical to an intense degree, hostile to religion and creeds, sarcastic, perverse; a liar, if Mercury be afflicted and most unamiable. Unfortunate long journeys, and if in a watery sign, danger of drowning; in the common signs and afflicting Mercury, hurts or malformation to feet or limbs.",
                         "Very conceited, pretentious, quick in anger and hasty in judgment, liable to much slander, an objectionable personality and aggressive; a man who aspires to martial honours and to rule others; a presumptuous man, pushful.",
                         "Bad and malicious friends; if afflicted, loss and injury through them.",
                         "Secret enemies; if afflicted, liability to false accusations and imprisonment; also assassination, if Mars afflicts the Sun or Moon. More than one royal personage has been assassinated who had Mars in the 12th and afflicting the luminaries."],
                     ["Great success in money matters, unless much afflicted; given to squandering and extravagance.",
                      "If in watery or movable signs, many short journeys; success and gain by writings, neighbours, and municipal affairs: gives a resolute and stable character.",
                      "Fortunate for the father, unless afflicted; success at the evening of life; acquisition of property; if afflicted, the reverse of all this.",
                      "Fond of company; gain by pleasure and speculation, if the sun be well-aspected. In the barren signs, this position denies offspring.",
                      "Bad health, if afflicted. In the fixed signs, all kinds of throat troubles, bladder affections, heart disease, weak back; in the common signs, liability to consumption and all kinds of chest disease, particularly if afflicted by Saturn or the Moon; in the cardinal signs, disordered system and stomach, head troubles.",
                      "Good for partnerships, honour, distinction, and business; opposition from powerful persons; a probable public position; a good marriage partner, independent in character.",
                      "Wasteful or lavish, husband or wife; rich partner in marriage, gain by will or legacy, if well-aspected.",
                      "In mind firm, noble, constant, and just; of a sincere and devout character. In watery signs, successful long journeys by sea; fortunate. in publishing; evilly aspected, there is little gain.",
                      "Success in business; honours; acquisition of money and good fortune comes to the mother, when well-aspected.",
                      "Faithful and powerful friends, from whom the native will benefit. If afflicted, loss by friends.",
                      "If afflicted, powerful secret enemies."], [
                         "Some prosperity, if well-aspected; if afflicted by Mars or Jupiter, the native will be extravagant.",
                         "Gives imagination, popularity, love of mirth and witticism; successful short journeys; if aspected by Mercury, poetical, musical, and literary talent; a fun-loving spirit prevails.",
                         "Success in the closing years of life, during which the native will be occupied by literature, art, or music; help from the father, who will be prosperous; if afflicted, the native is not prosperous.",
                         "Successful speculations; fond of all kinds of pleasures, amuse ments, and much given to the society of the other sex; loving, dutiful offspring.",
                         "Gain by servants or employees.",
                         "Success and happiness in marriage; fortunate in business, partnerships, and law; if Venus is afflicted, all this is overthrown.",
                         "Gain by marriage and legacies, unless afflicted.",
                         "Successful and pleasant journeys; the native will have great veneration for all things Divine; will be mirthful, poetic, conscientious, with artistic and musical ability; if aspected by Mars and Mercury, a keen sense of the ludicrous; well aspected by Mercury, beauty of thought, keen appreciation of the beautiful and a vivid imagination; if Venus be afflicted, the native rises not by his abilities.",
                         "A successful life, honour, love of pleasure and fortunate therein; good fortune to the mother, when well-aspected. This position often brings fame or auspicious notoriety.",
                         "Many friends, by whom the native gains, for they contribute to his happiness; realisation of hopes and wishes; not so, if Venus is afflicted.",
                         "Probable success in dealing in large cattle; if much afflicted, plotters and schemers will make trouble."],
                     ["If well-aspected, a modicum of success in literature and money matters.",
                      "Cultured, fond of scientific studies, clever; in the fixed signs, concentration of thought; in the movable signs, apt to see both sides of a question, but unable to do himself justice through lack of tenacity of purpose. The native is too versatile, with too rapid sequence of ideas.",
                      "If well-aspected, success as an estate agent, printer, engineer.",
                      "In barren signa, denies children; if afflicted in other signs, they may have some infirmity.",
                      "Troubles from servants, if afflicted. In the common signs, trouble with the respiratory organs; if much afflicted in 7. or my, mental disease is to be feared.",
                      "Rather clever wife or husband; if afflicted, quarrels with wife or husband; if well-aspected, the native might acquire a public post connected with science or literature.",
                      "Legacies and money by marriage if well-aspected: not otherwise.",
                      "Good mental abilities; intuitive, intellectual, scientific; the latter especially if in scientific signs; success in publishing and writing, but it ill-aspected there is little ability and little gain.",
                      "Literary ability; a teacher or schoolmaster. Intuitive and practical in judgment. Much depends on the sign Mercury occupies; if afflicted the abilities are poor.",
                      "Help from friends, unless this planet is afflicted.", "If afflicted, many secret enemies."], [
                         "Pence and prosperity if well-aspected; if afflicted by Saturn, without the support of Jupiter or Venus, the native will be poor.",
                         "Many successful short journeys; help from brethren and neighbours; a studious mind, unless afflicted.",
                         "Many changes; if well dignified and aspected, a successful farmer or builder. A competence is acquired.",
                         "Certainty of children, and in s or a very large family; afflicted by Saturn, with no good aspect from Jupiter or Venus, much sickness among them; success in speculation and in connection with places of amusement when well aspected.",
                         "If afflicted, ill-health. In common signs, liability to con sumption and lung disease; in the fixed signs, trouble with the throat, bladder and organic weakness of the heart; in the cardinal signs, derangement of the stomach and often headaches. Afflicted by Mars, inflammatory attacks and kidney disease: by Jupiter, the liver, blood and stomach are affected; by Mercury, liability to brain disease.",
                         "If unafflicted, a happy marriage; fortunate partnership; success in public dealing. The Moon is best, free from the influence of Uranus. Bad aspects of Saturn, Uranus or Mars to the Moon would cause infelicity and separation.",
                         "If unafflicted, money by marriage, gain by legacies, especially if befriended by Venus or Jupiter. If much afflicted by Mars, Saturn or Uranus, danger of serious accidents and a violent death; no money by marriage.",
                         "Long journeys and voyages; a studious mind. Aspected by Uranus, love of the occult, bigoted in religion and apt to change creed; aspected by Mercury, a quirk comprehensive mind.",
                         "If well-aspected, great success in life and in business as a merchant; if afflicted, little remunerative business; success to the mother: help from friends. Changes of avocation, if the Moon be in movable signs.",
                         "If well-dignified and aspected, great assistance from friends; if afflicted, loss by friends.",
                         "If afflicted, many secret foes."]]

Terms_Firmicus=[
[[6,"Jupiter"],[12,"Venus"],[20,"Mercury"],[25,"Mars"],[30,"Saturn"]]
,[[8,"Venus"],[14,"Mercury"],[22,"Jupiter"],[27,"Saturn"],[30,"Mars"]]
,[[6,"Mercury"],[12,"Jupiter"],[18,"Venus"],[24,"Mars"],[30,"Saturn"]]
,[[7,"Mars"],[13,"Venus"],[20,"Mercury"],[27,"Jupiter"],[30,"Saturn"]]
,[[6,"Jupiter"],[11,"Venus"],[18,"Saturn"],[24,"Mercury"],[30,"Mars"]]
,[[7,"Mercury"],[17,"Venus"],[21,"Jupiter"],[28,"Mars"],[30,"Saturn"]]
,[[6,"Saturn"],[14,"Mercury"],[21,"Jupiter"],[28,"Venus"],[30,"Mars"]]
,[[7,"Mars"],[11,"Venus"],[19,"Mercury"],[24,"Jupiter"],[30,"Saturn"]]
,[[12,"Jupiter"],[17,"Venus"],[23,"Mercury"],[27,"Saturn"],[30,"Mars"]]
,[[7,"Mercury"],[14,"Jupiter"],[22,"Venus"],[26,"Saturn"],[30,"Mars"]]
,[[7,"Mercury"],[13,"Venus"],[20,"Jupiter"],[25,"Mars"],[30,"Saturn"]]
,[[12,"Venus"],[16,"Jupiter"],[19,"Mercury"],[28,"Mars"],[30,"Saturn"]]
]

Empty_Full_Firmicus=[
[[3,"empty"],[5,"Senator"],[9,"empty"],[4,"Senacher"],[5,"empty"],[4,"Sentacher"]]
,[[3,"empty"],[7,"Suo"],[2,"empty"],[8,"Aryo"],[5,"empty"],[5,"Romanae"]]
,[[7,"Thesogar"],[2,"empty"],[5,"Ver"],[3,"empty"],[6,"Tepis"],[7,"empty"]]
,[[7,"empty"],[6,"Sothis"],[2,"empty"],[4,"Sith"],[2,"empty"],[9,"Thiumis"],[1,"empty"]]
,[[7,"Craumonis"],[4,"empty"],[3,"Sic"],[6,"empty"],[10,"Futile"]]
,[[5,"empty"],[5,"Thumis"],[2,"empty"],[6,"Tophicus"],[6,"empty"],[4,"Afut"],[3,"empty"]]
,[[5,"Seuichut"],[6,"empty"],[8,"Sepisent"],[3,"empty"],[6,"Senta"],[3,"empty"]]
,[[3,"empty"],[5,"Sentacer"],[6,"empty"],[6,"Tepisen"],[2,"empty"],[5,"Sentineu"],[3,"empty"]]
,[[9,"Eregbuo"],[3,"empty"],[7,"Sagon"],[4,"empty"],[7,"Chenene"]]
,[[7,"empty"],[3,"Themeso"],[5,"empty"],[4,"Epiemu"],[5,"empty"],[6,"Omol"]]
,[[4,"empty"],[5,"Oro"],[4,"empty"],[6,"Cratero"],[3,"empty"],[8,"Tepis"]]
,[[6,"empty"],[6,"Acha"],[3,"empty"],[5,"Tepibui"],[6,"empty"],[2,"Uiu"],[2,"Empty"]]
]
summ=0
for sign in Empty_Full_Firmicus:
    part1=0
    sum1=0
    for part in sign:
        if part[1] != "empty":
            part1+=part[0]
        sum1+=part[0]
    summ+=part1/sum1
print(summ/12)
house_meanings = [
    "The 1st house betokens the personal appearance and disposition, life, mind and character. Planets posited therein bear the most powerful influence upon the life and destiny of the nativo. Saturn or Mars in this house never fail to give accidents or indisposition, trouble, and a chequered career; while Jupiter and Venus therein, free from cross and opposition aspects, prefigure good health and fortune and a happy life.",
    "The 2nd house relates to wealth or property, prosperity or adversity, loss or gain. Saturn in this house, for instance, especially when in cross aspect to the Sun or Moon, causes pecuniary difficulties, losses of money; whilst Jupiter therein is a constant source of wealth; Mars there, would cause losses by rash enterprises.",
    "The 3rd house relates to brothers, sisters, relations, neighbours, short journeys and writings. Planets in this house influence the mind greatly. The Chaldeans read from this house the condition of kindred and of brethren. The Moon therein is a pregnant source of journeys; Saturn and Mars there, cause trouble from kindred, neighbours and short journeys. It is the house of mutations, according to Zael (a Chaldean writer).",
    "The 4th hour prefigures the father of the native, his own property and inheritance; it also indicates his position and condition at the end of life. Mars in this house causes trouble between the native and father; while Saturn there, indicates trouble in the eventide of life, sickness to the father; the acquisition of property if this planet is strong and well aspected, but loss if the contrary. It relates to the father's patrimony.",
    "The 5th house. All predictions relative to offspring, speculations, gaming, lotteries, etc., are formed from this house. It is the house of pleasure, enjoyment and merry-making of all sorts.",
    "The 6th house. This is associated with servants, cattle, sickness, diseases. Saturn in this house, conjoined with the Sun, would lower the vitality considerably, causing sickness and weak constitution; it brings trouble from servants and inferiors.",
    "The 7th house signifies marriage, description of wife or husband, partner ships, law suits, public enemies, opponents, public offices. Mars in this house causes domestic infelicity; Saturn there, indicates trouble, and delays marriage or prevents it altogether; Jupiter or Venus there, portray the best of husbands and wives, superlative happiness and felicity in marriage, success in public dealing.",
    "The 8th house. This shows the nature of death; it also relates to legacies, wills, property of the native's partner in marriage. Mars or Saturn there, cause loss and trouble concerning wills or the goods of the dead; whilst Jupiter in this house vouchsafes legacies and hereditaments.",
    "The 9th house tells us of the safety and success of long journeys either by sea or land; religion, dreams, preferments, etc. When a planet is in this house it has great influence on the mind of the native; for instance, Saturn there, adds gravity, reserve, fear of the unknown and reverence for Divine things; the native often becomes religious if Jupiter is posited therein, for this planet adda sincerity of soul, a serious spirit and the strongest regard for equity, the native is conscientious.",
    "The 10th house. This being the M.C. or meridian, and so most elevated part of the heavens, resolves all questions concerning persons in power and authority; it represents the native's mother, and has signification of honour and preferment (whether attainable or not), employment or profession, business and success therein. Saturn or Herschel in this house causes discredit in many ways; Jupiter there, vouchsafes honours and distinctions.",
    "The 11th house. Of friends, hopes and wishes; the friends correspond to the nature of the planets therein. Jupiter here, brings many good friends, sincere who contribute to one's happiness and good fortune; Mars and Saturn there, for instance, cause bad friends who cause trouble and disquietude.",
    "The 12th house. Called by the Chaldeans the house of tribulation, affliction, anxiety of mind, trouble, distress, imprisonment; it is the house of secret foes, backbiters, and of assassination, suicide, treason, and in fact all the misfortunes of mankind."]

secondary_directions_meaning=[["Sun",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Uranus","Changes, unsettledness, anxiety, sudden calamities, an unfortunate time for all new undertakings. The native is liable to accidents and sudden losses. In a female's natus it often causes a liaison or temptations thereto. Many leave their husbands under these directions. It sometimes causes a hasty marriage often regretted, or followed by a separation. The student must observe the houses in which the direction falls, and look for evil from things appertaining to those houses."],["Sun",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Uranus","If Uranus be prominent in a nativity, this aspect brings one much into prominence. It is a good direction for municipal or parliamentary honours. It often brings beneficial changes and journeys and local distinction. Civil servants under this direction obtain rapid preferment. ·with females it often causes attachments or liaisons and sometimes a hasty marriage, especially if Uranus occupies the 5th or 7th house."],["Sun",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Saturn","This is, perhaps, the most unfortunate direction one can come under, especially for health. The P., square and opposite exert most power; the conjunction, octile and tri-octile are not quite so strong. Death often results from this direction . When in the 2nd house, bankruptcy is almost certain to ensue. Mental anxiety, bereavement, indignities, loss of parents, grief and sorrow are generally caused by these aspects. The P. and conjunction of Sun and Saturn in Cancer, Capricorn or Aquarius, cause rheumatism. Females often lose their husbands through these directions. A gentleman who had Saturn in the 11th square, Sun and Moon), was nearly ruined by friends. When these aspects are in fixed or cardinal signs, accidents are to be feared ; in watery signs, death by water or liquids."],["Sun",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Saturn","Very fortunate for building or dealing in property or lands. Help from the people in whom Saturn's nature dominates, success, prosperity. These aspects incline one to be careful and accumulate property. They impart steadiness of character. With females one or other sometimes brings offers of marriage as well as good fortune."],["Sun",["Octile","Square","Tri-Octile","Opposition"],"Jupiter","Unfortunate for finance, law, business, and speculation, especially if the aspect be from 7th, 10th, 1st, or 2nd house. It debilitates the system and liver; causing pleurisy, stomach troubles, and poor blood. The native is sure to be much abused, and to meet with injury and contumely."],["Sun",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Jupiter","The most fortunate directions one can have. Health, honour, wealth. and prosperity ; help from powerful friends. When Jupiter occupies the 2nd or 10th house, during a P ., sextile, or trine, the native is remarkably successful in his pecuniary affairs. In a female's natus it is a sure sign of marriage or offers of marriage, if she is single and at a marriageable age."],["Sun",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mars","Inflammations, fevers, hurts, serious accidents,and often a violent death. In Gemini and Sagittarius, inflammation of the lungs and a disordered nervous system, falls; in the watery signs, death by drowning; in Virgo, danger of inflammation of the bowels ; in the fixed signs, great liability to accidents; in Leo or Aquarius, poasible syncope, if the heart is weak. Saturn causes sudden events. The native under these directions is rashly inclined, rushing head-long into quarrels and disputes. A person with Mars in the 2nd, during this direction, speculated rashly in business and soon became bankrupt. Amputations also are often necessary under this dirAction. It is more powerful if Mars affiicted one or both of the luminaries at birth. It operates in the same way with females; they are likely to quarrel with their husbands. Child-birth is likely to be fatal. A person under this direction, burst a blood-vessel near the nose which resulted in death. A woman whose Sun had progressed to conjunction and P. Mars in the 5th house, died in child-birth, in spite of the best medical aid."],["Sun",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mars","These bring physical activity and preferment, especially if in the army or navy; they incline to precipitancy in actions. The native will gain from those in whom Mars's nature dominate. Good for health and vitality ; with females, offers of marriage and new friends."],["Sun",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile"],"Venus","Success in dealing in jewellery, apparel, and fancy goods ; happiness and prosperity; love of amusement and pleasure. The principal aspects often cause marriage."],["Sun",["Octile","Square"],"Venus","Trouble through females, children, and young persons; very unfavourable, causing great disappointments."],["Sun",["Conjunction","Semi-Sextile","Sextile","Quintile"],"Mercury","Public honours in literature, art or science, inventions, literary undertakings, etc., if the nativity portrays an aptitude for these things. This direction is sure to bring much mental activity and increase of business. Artists receive distinction under it. The editor of an influential London paper resigned his post, and started a very successful magazine of his own under this direction. A publisher and printer floated a paper under the same, some ten years ago, and is now reputed to be very wealthy."],["Sun",["Octile","Square"],"Mercury","Trouble through writings, disappointments in literature, publishing, etc."],["Sun",["Cunjunction"],"Moon","Success and new undertakings. If Moon conjunction Sun occurred at birth, the native is certain to receive much assistance, pecuniary and otherwise, from the other sex. The native may marry a very wealthy person. This direction frequently causes marriage in a male's natus; in a female's it often causes indisposition, sometimes fevers; the health being much worse if this occurs in the 6th house. It is an unfavourable direction in a lady's nativity."],["Sun",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Moon","A very good direction for business and finance; it often brings credit, preferment, and success in business. If the native is in the employment of others, he is sure to be promoted, or receive marks of favour from his employers and superiors. The trine, P. and conjunction will bring marriage to either sex, especially if the Sun and Moon were in aspect at birth and dominant."],["Sun",["Octile","Square","Tri-Octile","Opposition"],"Moon","Unfortunate for business and finance; speculation should be avoided; unfortunate for dealing with superiors and persons in power. When the Sun or Moon occupies the 6th house, serious indisposition may ensue. This direction sometimes causes heavy bereavement. With females it often brings a severe illness, especially if the Moon squared or opposed the Sun at birth, or either occupied the 6th house at birth, or by direction. Of course the strength of the aspect must be considered. Again, when the direction occurs from angles, aspects will be found to operate much more powerfully than in other parts of the horoscope. Aspects from angles and cardinal signs are the most powerful, producing the most marked results. Aspects are also more powerful from fixed signs than from common ones. In every case the radical horoscope must be considered carefully; for, when this indicates a strong, healthy, disease-resisting constitution, a bad direction may produce only a slight illness or temporary indisposition. On the other hand, a weak, debilitated constitution, as portrayed by the affliction of the luminaries at birth by Saturn, may succumb to a direction which the more robust constitution would live through with ease. It is the same with regard to other affairs; for, when the horoscope portrays loss and ill-fortune, a bad direction will bring more ill-fortune than in the case where good fortune is portrayed at birth."],["Moon",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Uranus","Very unfavourable, unfortunate changes and journeys, mental anxiety and sometimes bereavement, odious notoriety when Uranus is dominant in the horoscope, suicide and intrigues with women when Uranus afflicted the Moon at birth. With females, troubles and annoyances from males, changes and troublesome journeys."],["Moon",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Uranus","These are favourable, and, unless Uranus affiicted the Moon at birth, may lead to a fortunate change and profitable journey, especially if Uranus or Moon occupies the 3rd or 9th house by direction or at birth. Like the evil aspects, it also tends to attachments with females ; it also brings unexpected good fortune."],["Moon",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Saturn","A very unfortunate direction. Losses, sorrows,disappointments, bereavements, serious illnesses, and to a weak constitution,sometimes death. Generally, bereavement, grief, despondency, and fear of impending calamity, especially if Saturn affiicted the Moon at birth. If Saturn or the Moon occupies the 2nd house, bankruptcy is to be feared."],["Moon",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Saturn","Success; the accumulation of wealth by personal industry; the native manages his affairs with tact and precision."],["Moon",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Jupiter","Exceptional success in business, preferment, and the increase of wealth; it also often brings marriage; with females it gives success, good health, new friends, and benefits from those in whom Jupiter's nature is dominant."],["Moon",["Octile","Square","Tri-Octile","Opposition"],"Jupiter","These aspects cause extravagance and losses in business. It is an unfortunate time for litigation; judges are sure to go against the native. With females it causes indisposition through irregular circulation and rush of blood to the head, particularly if the direction occur from cardinal signs;"],["Moon",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mars","These directions are remarkable for causing accidents, hurts, inflammatory diseases, and fevers. When under this aspect, especially if Mars affiicted the Moon at birth, the native is irritable, indiscreet, and quarrelsome; he may experience bladder and kidney troubles, especially if Mars occupies the 6th house. Persons under this direction should avoid disputes and dangerous places ; they may lose by fire, or theft. With females it acts the same as with males. Every person whose Moon was affiicted at birth by Mars, is liable, when under this direction, to death by violence, fever, or inflammation. A female in child-birth would be in imminent danger of death, especially if Mars occupies the 5th house."],["Moon",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mars","These bring physical activity, increase of business, and often very successful journeys. The native is courageous, self-confident, and adventuresome. This direction increases the disease-resisting faculties. It is the same with a female who, if Mars occupies the 5th house, is likely to form an attachment which may lead to trouble, especially if there are other indications of this in the nativity."],["Moon",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Sun","Help from friends. The P and conjunction cause marriage; the conjuction brings changes and new enterprises, much help from powerful and wealthy females if Moon conjunction Sun occurred at birth. The native may marry a wealthy person under this direction, especially if Moon conjunction Sun occurred at birth and near the 7th or 8th house. These aspects bring success in business, promotion, and general prosperity. The Moon conjunction Sun with females often causes indisposition, especially if they were in conjunction, square or opposition at birth, and either occupies the 6th house."],["Moon",["Octile","Square","Tri-Octile","Opposition"],"Sun","Unfortunate for native's affairs; bad for speculation; losses and annoyances are plentiful; danger of bereavement and ill-health, particularly in the case of a female. From angles, and especially from cardinal signs, this aspect is very powerful. The native should not push his affairs."],["Moon",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Venus","Love of pleasure and success therein. Merchants, jewellers, dealers in male and female attire, will be very prosperous. It points strongly to an increase of offspring, particularly when Venus or the Moon occupies the 5th house and children are not denied; it is also good for the health, dealing with females, and the purchasing of apparel."],["Moon",["Octile","Square","Tri-Octile","Opposition"],"Venus","Unfortunate; trouble, annoyances, and disappointments from females; sometimes bereavement. With females it causes temporary indisposition and a disordered system."],["Moon",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Mental activity, study, and, if the natus portray it, success in literature, science, or art. It may also bring a lawsuit or dealings with lawyers and literary men; fortunate for writings, agreements, gain from publishing, and applications for secretaryships."],["Moon",["Octile","Square","Tri-Octile","Opposition"],"Mercury","Unfortunate for writings, law, agreements, and literary undertakings; difficulty in passing examinations, etc."],["Moon",["Conjunction","Semi-Sextile","Sextile","Trine"],"Moon","Brings success, journeys (especially if the Moon occupied the 3rd, 9th, or 12th house), and new friends of both sexes."],["Moon",["Octile","Square","Tri-Octile","Opposition"],"Moon","Unfortunate, annoyances through females, slight temporary indisposition."],["Uranus",["Conjunction","Square","Opposition"],"Saturn","These are powerful when Uranus and Saturn are dominant in the figure. In the 7th, unhappiness in marriage, and a very bad marriage partner; in the 10th, unpopularity and disagreeable rumours."],["Uranus",["Sextile","Trine"],"Saturn","Undesirable, though they tend to stability and power."],["Uranus",["Conjunction","Sextile","Trine"],"Jupiter","These often bring money or legacies."],["Uranus",["Octile","Square","Tri-Octile","Opposition"],"Jupiter","Bad for litigation, loss of money."],["Uranus",["Sextile","Trine"],"Mars","Success in antagonisms, if Mars be dominant and well-aspected."],["Uranus",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mars","Unfortunate. In the 10th, unpopularity, quarrels, troubles in business; in the 7th, worries, antagonisms, quarrels with the marriage partner; in the 12th, active secret foes and danger of imprisonment. A man with Mars in the 12th opposition Uranus suffered imprisonment when the Moon by progressive motion reached the square of Mars and Uranus."],["Uranus",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Venus","Trouble through the other sex; sometimes a liaison or scandal. Females under this direction should be very careful in their dealings with males."],["Uranus",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Venus","A strong love of the other sex is likely to result."],["Uranus",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mercury","Often causes newspaper controversy; trouble through writings, great inclination for occult studies; the mind is wayward, sarcastic, and uncertain; reverses in literature, opposition and hostility in various ways are likely."],["Uranus",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Strong inclination for study, especially of science, human nature, occultism, astrology, phrenology, etc. The native gains much by observation and practical experience, is inclined to originality of thought and indifference to creeds; it also gives tact and precision."],["Saturn",["Octile","Square","Tri-Octile","Opposition"],"Jupiter","Unfortunate for law and litigation. The native will experience losses and obstacles in various ways, unsuccessful investments, and loss by bank failures."],["Saturn",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Jupiter","Often brings inheritance, legacies, etc.; also successful lawsuits, honours, popularity, and church preferment."],["Saturn",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mars","Great malice and violence. If Mars or Saturn occupies the 1st, 10th, 3rd or 9th house, the native may commit a crime (perhaps murder), may meet with a serious accident, be maimed, hanged, or imprisoned. An acquaintance who had Mars square Saturn, from 10th and 1st houses, met with a serious accident, when this aspect became complete, and was crippled for life; in this instance Mars afilicted the Moon at birth."],["Saturn",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mars","Gives courage, firmness, stability, and frequently local distinction."],["Saturn",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Venus","Trouble through the other sex. This direction is disastrous for courtship, and often causes grief and bereavement; also disreputable habits and frequent scandal; certainly disappointment."],["Saturn",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Venus","This inclines to reserve, modesty, and good conduct; also to constancy in attachment."],["Saturn",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mercury","The temper is very captious. The native is liable to pilfer, or take part in illicit transactions, which may bring him into trouble; especially if Mercury and Saturn are dominant in the horoscope and Mercury be afflicted at birth. Good aspects of Jupiter and Venus at birth counteract the tendency to fraud, etc."],["Saturn",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Careful, reserved, cautious; tact in managing affairs, serious, thoughtful."],["Jupiter",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mars","Native is vain and adventuresome, hasty, extravagant, and reckless. It is bad for lawsuits and contention. In the 2nd or 8th house it causes great extravagance."],["Jupiter",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mars","Promotion, honour, much success. If Jupiter is in the 2nd, pecuniary success. A person with Jupiter in the 5th under this direction won a large sum in turf speculation."],["Jupiter",["Octile","Square","Tri-Octile","Opposition"],"Venus","Pride, extravagance over dress, ornaments, amusements and females."],["Jupiter",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Venus","Social success, and in dealings with females."],["Jupiter",["Octile","Square","Tri-Octile","Opposition"],"Mercury","Mental trouble, wrong notions in general. An acquaintance with Mercury opposition Jupiter from 1st and 7th houses suffered mental derangement, and had much trouble in his transactions, this position being very bad for litigation, and portraying heavy losses. Litigants generally have the Sun and Mercury afflicted by Jupiter either at birth or by direction."],["Jupiter",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Credit and distinction in literature or public speaking, and gain therefrom. This aspect elevates the mind, makes the native prudent and sincere, and inspires successful plans."],["Mars",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Venus","Flirtation and sometimes scandal. If either or both are in the 7th, domestic quarrels will take place. When Mars occupies the 5th in the case of a female, trouble and misfortune through the other sex are portrayed."],["Mars",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Venus","Extravagance, love of pleasure and the other sex; it often brings females to grief."],["Mars",["Conjunction","Octile","Square","Tri-Octile","Opposition"],"Mercury","The temper is short; the native may commit a theft if Mercury was afflicted at birth; danger of quarrels, disputes, or (if the nativity denotes it) lawsuits."],["Mars",["Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Mental energy; the mind is quick, sharp, and penetrating; the native is precise, and often obtains distinction in mechanical science or engineering."],["Venus",["Conjunction","Semi-Sextile","Sextile","Quintile","Bi-Quintile","Trine"],"Mercury","Very good; distinction in poetry, music, or art, if the nativity shows ability for these things; the native is merry, witty, laughter-loving, and susceptible to poetical inspiration. A friend with Venus in the 9th at birth, P to Mercury, obtained more than local distinction in poetry and music under this direction."]]


persons_data = []

choice = 0
UI_size = 42


def tit(Text):
    print('{:{}^{}} '.format(Text, "*", UI_size))

def bod(Text):
    print("* {:{}<{}}*".format(Text, " ", UI_size - 3))

def bod_format(Text):
    text_array=Text.split(" ")
    text2="    "
    for elem in text_array:
        if len(text2)+1+len(elem)<UI_size-3:
            text2+=" "+elem
        else:
            bod(text2)
            text2=elem
    bod(text2)

def opt(*arg):
    for num in range(0, len(arg)):
        print("*{:{}<{}}*".format(" [{}] {}".format(num + 1, arg[num]), " ", UI_size - 2))

def end():
    print("*" * UI_size)
    print("\n")

def endl():
    global choice
    print("*" * UI_size)
    choice = input(">>> ")
    print("\n")


# How to Display: Desu
# How to do padding
# Example: $one:{$two}$three{$four}
# $one:     Text
# $two:     filler char or text
# $three:   can be < for left padding, > for right padding, and = for center padding
# $four:    Maximum limit of filler char, is a number
# Template: print( '{:{}^{}}' .format("","*",35))
# Template: print("*{:{}<{}}*".format(""," ",33))
# Template: print("*"*35)

# tit("")
# opt("")
# end()
# endl()

def house_codes_interp(house_codes):
    codes = house_codes.lower().split(" ")
    ura = ""
    for i in range(0, len(codes)):
        if "ura" in codes[i]:
            ura = codes[i]
    sat = ""
    for i in range(0, len(codes)):
        if "sat" in codes[i]:
            sat = codes[i]
    jup = ""
    for i in range(0, len(codes)):
        if "jup" in codes[i]:
            jup = codes[i]
    mar = ""
    for i in range(0, len(codes)):
        if "mar" in codes[i]:
            mar = codes[i]
    sun = ""
    for i in range(0, len(codes)):
        if "sun" in codes[i]:
            sun = codes[i]
    ven = ""
    for i in range(0, len(codes)):
        if "ven" in codes[i]:
            ven = codes[i]
    mer = ""
    for i in range(0, len(codes)):
        if "mer" in codes[i]:
            mer = codes[i]
    moo = ""
    for i in range(0, len(codes)):
        if "moo" in codes[i]:
            moo = codes[i]

    ura = code_to_array(ura)
    sat = code_to_array(sat)
    jup = code_to_array(jup)
    mar = code_to_array(mar)
    sun = code_to_array(sun)
    ven = code_to_array(ven)
    mer = code_to_array(mer)
    moo = code_to_array(moo)

    tit(" Uranus [{}]".format(toRoman(ura[1])))
    array_to_meaning(ura)
    tit(" Saturn [{}]".format(toRoman(sat[1])))
    array_to_meaning(sat)
    tit(" Jupiter [{}]".format(toRoman(jup[1])))
    array_to_meaning(jup)
    tit(" Mars [{}]".format(toRoman(mar[1])))
    array_to_meaning(mar)
    tit(" Sun [{}] ".format(toRoman(sun[1])))
    array_to_meaning(sun)
    tit(" Venus [{}] ".format(toRoman(ven[1])))
    array_to_meaning(ven)
    tit(" Mercury [{}] ".format(toRoman(mer[1])))
    array_to_meaning(mer)
    tit(" Moon [{}] ".format(toRoman(moo[1])))
    array_to_meaning(moo)


def code_to_array(code):
    if len(code) > 4:
        if code[4].isalpha():
            return [code[:3], 1, code[4:]]
        else:
            return [code[:3], int(code[3:])]
    else:
        return [code[:3], int(code[3:])]


def array_to_meaning(array):
    if (array[1] == 1):
        bod_format(planets_on_ascendant[pla_to_num(array[0]) - 1][sig_to_num(array[2]) - 1])
    else:
        bod_format(planets_on_houses[pla_to_num(array[0]) - 1][array[1] - 2])


def sig_to_num(sign):
    if (sign == "are"):
        return 1
    if (sign == "tau"):
        return 2
    if (sign == "gem"):
        return 3
    if (sign == "can"):
        return 4
    if (sign == "leo"):
        return 5
    if (sign == "vir"):
        return 6
    if (sign == "lib"):
        return 7
    if (sign == "sco"):
        return 8
    if (sign == "sag"):
        return 9
    if (sign == "cap"):
        return 10
    if (sign == "aqu"):
        return 11
    if (sign == "pis"):
        return 12


def pla_to_num(planet):
    planetas = {
        'ura': 1,
        'sat': 2,
        'jup': 3,
        'mar': 4,
        'sun': 5,
        'ven': 6,
        'mer': 7,
        'moo': 8,
    }
    a = planet.strip()[:3].lower()
    try:
        ez = planetas[a]
        return (ez)
    except:
        raise ValueError('Not a planet')

def aspect_to_deg(aspect):
    degrees = {
        'conjunction': 0,
        'semi-sextile': 30,
        'octile': 45,
        'sextile': 60,
        'quintile': 72,
        'square': 90,
        'trine': 120,
        'tri-octile': 135,
        'bi-quintile': 144,
        'opposition': 180,
    }
    a = aspect
    try:
        ez = degrees[a.lower()]
        return (ez)
    except:
        raise ValueError('Not an aspect.')

def init():
    if (os.path.isfile("powhouast.txt")):
        read_data()

aspects_data=[]

def read_aspects(year,angles,planets_a):
    global aspects_data
    if planets_a=="":
        planets_list=["Pluto","Neptune","Uranus","Saturn","Jupiter","Mars","Sun","Venus","Mercury","Moon"]
    else:
        planets_list=planets_a.split()
    if angles=="":
        angles_list=["000", "030", "045", "060", "072","090", "120", "135", "144", "180"]
    else:
        angles_list = angles.split()

    aspects_data=[]
    temp=[]
    with open("aspects/{}.txt".format(str(year))) as f:
        temp= f.read().splitlines()
    for aspect in temp:
        as_split=aspect.split()
        if as_split[1] in angles_list and as_split[0] in planets_list and as_split[2] in planets_list:
            aspects_data.append(as_split)

#['Moon', '072', 'Mercury', '12/30/2022', '05:49:04']
def aspect_to_datetime(aspect):
    aspect_date = list(map(int, aspect[3].split("/")))
    aspect_time = list(map(int, aspect[4].split(":")))

    return datetime(year=aspect_date[2],month=aspect_date[0],day=aspect_date[1],hour=aspect_time[0],minute=aspect_time[1],second=aspect_time[2])

#2022-08-13 09:12:48
def input1_to_datetime(input):
    dated=input.split()
    aspect_date = list(map(int, dated[0].split("-")))
    aspect_time = list(map(int, dated[1].split(":")))

    return datetime(year=aspect_date[0],month=aspect_date[1],day=aspect_date[2],hour=aspect_time[0],minute=aspect_time[1],second=aspect_time[2])

def find_next_aspects(datetime_now,array_size,datetime_start):
    global aspects_data
    aspects_output=[]
    if datetime_start=="":
        date_start=datetime_now
    else:
        date_start=input1_to_datetime(datetime_start)

    if array_size=="":
        iter=1
    else:
        iter=int(array_size)

    for aspect in aspects_data:
        if date_start<aspect_to_datetime(aspect) and iter!=0:
            aspects_output.append(aspect)
            iter-=1

    return aspects_output

def read_data():
    global persons_data
    f = open("powhouast.txt", "r")
    persons_data = eval(f.readlines()[0])
    f.close()


def data_save():
    global persons_data
    f = open("powhouast.txt", "w+")
    f.write(str(persons_data))
    f.close()

import re

def input_to_filtered_aspects(input):
    output=input.replace(" ","").split("Find»")
    output2=[]
    output3=[]
    output4=[]
    for element in output:
        output2.append(re.findall('[A-Z][^A-Z]*', element ))
    for element in output2:
        newelement=[]
        if len(element)==3:
            for num1 in range(0,3):
                if num1==2:
                    for num2 in range(0,len(element[num1])):
                        if element[num1][num2].isdigit():
                            newelement.append(element[num1][:num2])
                            newelement.append(element[num1][num2:].replace("°","° "))
                            break
                else:
                    newelement.append(element[num1])
        output3.append(newelement)

    for element in output3:
        element2=[]
        if len(element)==5:
            element2+=[element[0],element[1]+element[2],element[3]]
        else:
            element2=element
        if element2!=[] and element2[0] in planets and element2[2] in planets:
            output4.append(element2)

    return output4

def orb_to_deg(nums):
    if isinstance(nums,str):
        return nums
    else:
        dec=math.modf(nums)
        output=""
        if nums<0:
            output+="-"
        output+=str(abs(int(dec[1])))+"° "
        output+=str(abs(int(dec[0]*60)))+"'"
        return output

def num_to_deg(num):
    num1=math.modf(num)
    num2=math.modf(num1[0]*60)
    degr=int(num1[1])
    minu=int(num2[1])
    seco=int(num2[0]*60)
    return "{}° {}' {}".format(degr,minu,seco)+u'\u0022'


def date_array_to_datetime(date_array):
    return datetime(*date_array[1:6])

def datetime_to_date_array(name,date_time,place):
    return [name,date_time.year,date_time.month,date_time.day,date_time.hour,date_time.minute,place]

def sign_function(x):
    if x > 0: return 1
    elif x == 0: return 0
    else: return -1

def find_orb(planet1_pos,planet2_pos,aspect):
    #asprint("Planet 1 Pos: {}".format(orb_to_deg(planet1_pos)))
    #asprint("Planet 1 Pos: {}".format(orb_to_deg(planet1_pos)))
    if abs(planet1_pos-planet2_pos)>180:
        if planet1_pos>planet2_pos:
            return abs(planet1_pos-360 - planet2_pos) - aspect_to_deg(aspect)
        else:
            return abs(planet2_pos-360 - planet1_pos) - aspect_to_deg(aspect)
    else:
        return abs(planet1_pos-planet2_pos)-aspect_to_deg(aspect)

def transit_day_increment(planet1,aspect,planet2,orb,birth_array):
    sign=sign_function(orb)
    day_increment=0
    returns=True
    direction=""
    while(returns):
        future=KrInstance(*datetime_to_date_array(birth_array[0],date_array_to_datetime(birth_array)+timedelta(days=day_increment),birth_array[6]))
        future_pos=[future.uranus.abs_pos,future.saturn.abs_pos,future.jupiter.abs_pos,future.mars.abs_pos,future.sun.abs_pos,future.venus.abs_pos,future.mercury.abs_pos,future.moon.abs_pos]
        future_orb=find_orb(future_pos[pla_to_num(planet1)-1],future_pos[pla_to_num(planet2)-1],aspect)
        #print("Future Date {}".format(date_array_to_datetime(birth_array)+timedelta(days=day_increment)))
        #print("Future Orb {}".format(future_orb))
        if sign_function(future_orb)!=sign:
            day_increment -= 1
            returns=False
            direction="right"
            break

        past = KrInstance(*datetime_to_date_array(birth_array[0], date_array_to_datetime(birth_array) - timedelta(days=day_increment),birth_array[6]))
        past_pos = [past.uranus.abs_pos, past.saturn.abs_pos, past.jupiter.abs_pos, past.mars.abs_pos,
                      past.sun.abs_pos, past.venus.abs_pos, past.mercury.abs_pos, past.moon.abs_pos]
        past_orb = find_orb(past_pos[pla_to_num(planet1)-1], past_pos[pla_to_num(planet2)-1], aspect)
        #print("Past Date {}".format(date_array_to_datetime(birth_array) - timedelta(days=day_increment)))
        #print("Past Orb {}".format(past_orb))
        if sign_function(past_orb) != sign:
            minute_increment = -(day_increment - 1)
            returns = False
            direction="left"
            break
        day_increment += 1

    return [day_increment,sign,direction]
        #for aspectkery in NatalAspects(KrInstance(*datetime_to_date_array(birth_array[0],date_array_to_datetime(birth_array)+timedelta(day_increment),birth_array[7]))).get_all_aspects():


def transit_hour_increment(birth_array,planet1,aspect,planet2,sign,day_increment,direction):
    inc=1
    if direction=="left":
        inc=-1
    hour_increment=0
    returns=True

    while (returns):
        future = KrInstance(
            *datetime_to_date_array(birth_array[0], date_array_to_datetime(birth_array) + timedelta(day_increment,hours=hour_increment),
                                    birth_array[6]))
        future_pos = [future.uranus.abs_pos, future.saturn.abs_pos, future.jupiter.abs_pos, future.mars.abs_pos,
                      future.sun.abs_pos, future.venus.abs_pos, future.mercury.abs_pos, future.moon.abs_pos]
        future_orb = find_orb(future_pos[pla_to_num(planet1) - 1], future_pos[pla_to_num(planet2) - 1], aspect)
        if sign_function(future_orb) != sign:
            hour_increment -= inc
            returns = False
            break
        hour_increment+= inc

    return hour_increment

def transit_minute_increment(birth_array,planet1,aspect,planet2,sign,day_increment,hour_increment,direction):
    inc = 1
    if direction == "left":
        inc = -1
    minute_increment = 0
    returns = True

    while (returns):
        future = KrInstance(
            *datetime_to_date_array(birth_array[0], date_array_to_datetime(birth_array) + timedelta(days=day_increment,hours=hour_increment,minutes=minute_increment),
                                    birth_array[6]))
        future_pos = [future.uranus.abs_pos, future.saturn.abs_pos, future.jupiter.abs_pos, future.mars.abs_pos,
                      future.sun.abs_pos, future.venus.abs_pos, future.mercury.abs_pos, future.moon.abs_pos]
        future_orb = find_orb(future_pos[pla_to_num(planet1) - 1], future_pos[pla_to_num(planet2) - 1], aspect)
        if sign_function(future_orb) != sign:
            minute_increment -= inc
            returns = False
            break
        minute_increment += inc
    return minute_increment

def transit_datetime(planet1,aspect,planet2,orb,birth_array):
    if aspect=="Opposition" or aspect=="Conjunction":
        return aspect
    else:
        data1=transit_day_increment(planet1,aspect,planet2,orb,birth_array)
        day_increment,sign,direction=data1[0],data1[1],data1[2]
        hour_increment=transit_hour_increment(birth_array,planet1,aspect,planet2,sign,day_increment,direction)
        minute_increment=transit_minute_increment(birth_array,planet1,aspect,planet2,sign,day_increment,hour_increment,direction)

        return(date_array_to_datetime(birth_array)+timedelta(days=day_increment,hours=hour_increment,minutes=minute_increment))
    #return 1


def aspect_status(planet1,aspect,planet2,orb,birth_array):
    global pos_data
    if birth_array[7]==False:
        return "N/A"
    else:
    #transit_date=KrInstance(*datetime_to_date_array(birth_array[0],transit_datetime(planet1,aspect,planet2,orb,birth_array),birth_array[7]))
        return transit_datetime(planet1,aspect,planet2,orb,birth_array)
    #pos_data[1]=[[pos1_kery.uranus.abs_pos,pos1_kery.saturn.abs_pos,pos1_kery.jupiter.abs_pos,pos1_kery.mars.abs_pos,pos1_kery.sun.abs_pos,pos1_kery.venus.abs_pos,pos1_kery.mercury.abs_pos,pos1_kery.moon.abs_pos],[pos2_kery.uranus.abs_pos,pos2_kery.saturn.abs_pos,pos2_kery.jupiter.abs_pos,pos2_kery.mars.abs_pos,pos2_kery.sun.abs_pos,pos2_kery.venus.abs_pos,pos2_kery.mercury.abs_pos,pos2_kery.moon.abs_pos]]

def classify_aspect(aspect):
    major=["conjunction","sextile","square","trine","oppositon"]
    if aspect in major:
        return "Major Aspect"
    else:
        return "Minor Aspect"

def aspect_to_secondary_direction_meaning(aspect,birth_array):
    global secondary_directions_meaning
    if birth_array=="AstroSeekCode":
        tit("{} ({}) {} [{}]".format(aspect[0], aspect[1].lower(), aspect[2], aspect[3]))
    if birth_array=="AspectOnly":
        tit(" [ {} ({}) {} ] ".format(aspect[0], aspect[1].lower(), aspect[2]))
    else:
        tit("{} ({}) {} [{}]".format(aspect[0],aspect[1].lower(),aspect[2],orb_to_deg(aspect[3])))
    #tit("({})".format(aspect_status(aspect[0],aspect[1],aspect[2],aspect[3],birth_array)))
    output="No info."
    for meaning in secondary_directions_meaning:
        if (aspect[0] in meaning[0] and aspect[1] in meaning [1] and aspect[2] in meaning[2]):
            output=meaning[3]

        if (aspect[0] in "Sun" and aspect[2] in "Moon") or (aspect[0] in "Moon" and aspect[2] in "Sun") or (aspect[0] in "Moon" and aspect[2] in "Moon"):
            pass
        else:
            if (aspect[2] in meaning[0] and aspect[1] in meaning[1] and aspect[0] in meaning[2]):
                output=meaning[3]
    tit(" [ {} ] ".format(classify_aspect(aspect[1].lower())))
    bod_format(output)
    #bod(" ")

def toRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    output=""
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            output+=sym[i]
            div -= 1
        i -= 1

    return(output)

def secondary_code_to_meaning(code,birth_array):
    if birth_array=="AstroSeekCode":
        for aspect in code:
            aspect_to_secondary_direction_meaning(aspect,"AstroSeekCode")
    else:
        for aspect in code:
            aspect_to_secondary_direction_meaning(aspect,birth_array)

def birth_info_to_array(birth_name,birth_info):
    info_array=birth_info.replace(",","").split(" ")
    time=["12","0"]
    location=info_array[3]
    isTimeGiven=False
    if len(info_array)==5:
        location=info_array[4]
        time=info_array[3].split(":")
        isTimeGiven=True
    return [birth_name,int(info_array[2]),mtn(info_array[0]),int(info_array[1]),int(time[0]),int(time[1]),location,isTimeGiven]

def mtn(x):
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    a = x.strip()[:3].lower()
    try:
        ez = months[a]
        return (ez)
    except:
        raise ValueError('Not a month')

def ata(x):
    aspects = {
        '000': "Conjunction",
        '030': "Semi-Sextile",
        '045': "Octile",
        '060':"Sextile",
         '072':"Quintile",
         '090':"Square",
         '120':"Trine",
         '144':"Bi-Quintile",
         '135':"Sesquiquadrate",
         '180':"Opposition"
        }
    a = x.strip()[:3].lower()
    try:
        ez = aspects[a]
        return (ez)
    except:
        raise ValueError('Not an aspect')

def position_to_term(planet_data):
    global Terms_Firmicus
    sign_data=Terms_Firmicus[planet_data["sign_num"]]
    for term in sign_data:
        if planet_data["position"]<term[0]:
            return term[1]

def term_locations(person):
    tit(" [Terms of] ")
    tit(" [Houses] ")
    bod("Ascendant = {}".format(position_to_term(person.first_house)))
    bod("Second House = {}".format(position_to_term(person.second_house)))
    bod("Third House = {}".format(position_to_term(person.third_house)))
    bod("Imum Coeli = {}".format(position_to_term(person.fourth_house)))
    bod("Fifth House = {}".format(position_to_term(person.fifth_house)))
    bod("Sixth House = {}".format(position_to_term(person.sixth_house)))
    bod("Descendant = {}".format(position_to_term(person.seventh_house)))
    bod("Eight House = {}".format(position_to_term(person.eighth_house)))
    bod("Ninth House = {}".format(position_to_term(person.ninth_house)))
    bod("Midheven = {}".format(position_to_term(person.tenth_house)))
    bod("Eleventh House = {}".format(position_to_term(person.eleventh_house)))
    bod("Twelfth = {}".format(position_to_term(person.twelfth_house)))
    tit(" [Terms of] ")
    tit(" [Planets] ")
    bod("Pluto = {}".format(position_to_term(person.pluto)))
    bod("Neptune = {}".format(position_to_term(person.neptune)))
    bod("Uranus = {}".format(position_to_term(person.uranus)))
    bod("Saturn = {}".format(position_to_term(person.saturn)))
    bod("Jupiter = {}".format(position_to_term(person.jupiter)))
    bod("Mars = {}".format(position_to_term(person.mars)))
    bod("Sun = {}".format(position_to_term(person.sun)))
    bod("Venus = {}".format(position_to_term(person.venus)))
    bod("Mercury = {}".format(position_to_term(person.mercury)))
    bod("Moon = {}".format(position_to_term(person.moon)))

def position_to_empty_or_full(planet_data):
    global Empty_Full_Firmicus
    total=0
    for part in Empty_Full_Firmicus[planet_data["sign_num"]]:
        total+=part[0]
    the_sum=0
    for part in Empty_Full_Firmicus[planet_data["sign_num"]]:
        the_sum+=part[0]
        if planet_data["position"]<the_sum/total*30:
            return part[1]

def empty_or_full(person):
    tit(" [Empty or Full] ")
    tit(" [Houses] ")
    bod("Ascendant = {}".format(position_to_empty_or_full(person.first_house)))
    bod("Second House = {}".format(position_to_empty_or_full(person.second_house)))
    bod("Third House = {}".format(position_to_empty_or_full(person.third_house)))
    bod("Imum Coeli = {}".format(position_to_empty_or_full(person.fourth_house)))
    bod("Fifth House = {}".format(position_to_empty_or_full(person.fifth_house)))
    bod("Sixth House = {}".format(position_to_empty_or_full(person.sixth_house)))
    bod("Descendant = {}".format(position_to_empty_or_full(person.seventh_house)))
    bod("Eight House = {}".format(position_to_empty_or_full(person.eighth_house)))
    bod("Ninth House = {}".format(position_to_empty_or_full(person.ninth_house)))
    bod("Midheven = {}".format(position_to_empty_or_full(person.tenth_house)))
    bod("Eleventh House = {}".format(position_to_empty_or_full(person.eleventh_house)))
    bod("Twelfth = {}".format(position_to_empty_or_full(person.twelfth_house)))
    tit(" [Empty or Full] ")
    tit(" [Planets] ")
    bod("Pluto = {}".format(position_to_empty_or_full(person.pluto)))
    bod("Neptune = {}".format(position_to_empty_or_full(person.neptune)))
    bod("Uranus = {}".format(position_to_empty_or_full(person.uranus)))
    bod("Saturn = {}".format(position_to_empty_or_full(person.saturn)))
    bod("Jupiter = {}".format(position_to_empty_or_full(person.jupiter)))
    bod("Mars = {}".format(position_to_empty_or_full(person.mars)))
    bod("Sun = {}".format(position_to_empty_or_full(person.sun)))
    bod("Venus = {}".format(position_to_empty_or_full(person.venus)))
    bod("Mercury = {}".format(position_to_empty_or_full(person.mercury)))
    bod("Moon = {}".format(position_to_empty_or_full(person.moon)))

def birth_array_to_house_code(birth_array):
    if birth_array[7]==False:
        tit("Information")
        bod_format("No House Interpretation as there is no Birth Time or Place provided")
        endl()
    else:
        person = KrInstance(*birth_array[:7])
        print(person.uranus)
        code=""
        code+= "ura"+str(ordtocard(person.uranus["house"]))
        if ordtocard(person.uranus["house"])==1:
            code+=person.uranus["sign"]
        code += " sat" + str(ordtocard(person.saturn["house"]))
        if ordtocard(person.saturn["house"]) == 1:
            code += person.saturn["sign"]
        code += " jup" + str(ordtocard(person.jupiter["house"]))
        if ordtocard(person.jupiter["house"]) == 1:
            code += person.jupiter["sign"]
        code += " mar" + str(ordtocard(person.mars["house"]))
        if ordtocard(person.mars["house"]) == 1:
            code += person.mars["sign"]
        code += " sun" + str(ordtocard(person.sun["house"]))
        if ordtocard(person.sun["house"]) == 1:
            code += person.sun["sign"]
        code += " ven" + str(ordtocard(person.venus["house"]))
        if ordtocard(person.venus["house"]) == 1:
            code += person.venus["sign"]
        code += " mer" + str(ordtocard(person.mercury["house"]))
        if ordtocard(person.mercury["house"]) == 1:
            code += person.mercury["sign"]
        code += " moo" + str(ordtocard(person.moon["house"]))
        if ordtocard(person.moon["house"]) == 1:
            code += person.moon["sign"]
        house_codes_interp(code)
        term_locations(person)
        empty_or_full(person)

def ordtocard(x):
    Ordinals = {
        'fir': 1,
        'sec': 2,
        'thi': 3,
        'fou': 4,
        'fif': 5,
        'six': 6,
        'sev': 7,
        'eig': 8,
        'nin': 9,
        'ten': 10,
        'ele': 11,
        'twe': 12
    }
    a = x.strip()[:3].lower()
    try:
        ez = Ordinals[a]
        return (ez)
    except:
        raise ValueError('Not an Ordinal')

def aspect_to_astroseek(aspect):
    output=aspect
    if output == "semi-square":
        output="octile"
    if output == "sesquiquadrate":
        output = "tri-octile"
    if output == "biquintile":
        output = "bi-quintile"
    output=output.split("-")
    output_final=output[0].capitalize()
    if len(output)==2:
        output_final+="-"+output[1].capitalize()
    return output_final

def batsc2(kerykeion_aspects):
    aspects=[]
    #for i in kerykeion_aspects:
        #print(i)
    for aspect in kerykeion_aspects:
        if aspect["p1_name"] in planets and not aspect["aspect"] in aspect_names and aspect["p2_name"] in planets:
            aspects.append([aspect["p1_name"],aspect_to_astroseek(aspect["aspect"]),aspect["p2_name"],aspect["orbit"]])
    return aspects


def birth_array_to_secondary_code(birth_array):
    secondary_code=""
    if birth_array[7]==True:
        person= KrInstance(*birth_array[:7])
        aspects=NatalAspects(person).get_all_aspects()
        return (batsc2(aspects))

    else:
        person1st= KrInstance(*birth_array[:4],0,0,birth_array[6])
        person2nd= KrInstance(*birth_array[:4],23,59,birth_array[6])
        aspects1=batsc2(NatalAspects(person1st).get_all_aspects())
        aspects2=batsc2(NatalAspects(person2nd).get_all_aspects())
        aspects=[]
        for aspect in aspects1:
            for aspect2 in aspects2:
                if aspect[0] in aspect2[0] and aspect[1] in aspect[1] and aspect[2] in aspect[2]:
                    aspects.append(aspect[:-1]+["N/A"])
                elif aspect[2] in aspect2[0] and aspect[1] in aspect[1] and aspect[0] in aspect[2]:
                    aspects.append(aspect[:-1]+["N/A"])
        #removes duplicates
        import itertools
        aspects.sort()
        aspects=list(aspects for aspects, _ in itertools.groupby(aspects))
        return aspects

def over_360_angle(num):
    if num>360:
        return num-360
    else:
        return num

def right_planet(planet_1,planet_2,angle_diff):
    if math.fabs(over_360_angle(planet_1[1]+angle_diff)-planet_2[1])<math.fabs(over_360_angle(planet_2[1]+angle_diff)-planet_1[1]):
        return [planet_1[0],planet_2[0]]
    else:
        return [planet_2[0], planet_1[0]]

def aspect_to_angle(aspect,planets_data):
    planet_1=[aspect[0]]
    planet_2=[aspect[2]]
    for planet in planets_data:
        if planet.name==planet_1[0]:
            planet_1.append(planet.abs_pos)
        if planet.name==planet_2[0]:
            planet_2.append(planet.abs_pos)
        if len(planet_1)==2 and len(planet_2)==2:
            break
    if planet_1[1]>planet_2[1]:
        angle_diff=over_360_angle(planet_1[1]-planet_2[1])
    else:
        angle_diff = over_360_angle(planet_2[1] - planet_1[1])
    if angle_diff>180:
        angle_diff=360-angle_diff
    output=right_planet(planet_1,planet_2,angle_diff)+[num_to_deg(angle_diff)]
    return output

#print_all_data(KrInstance(*['Barly Algones Dinalo', 2000, 9, 19, 2, 32, 'Cebu', True][:7]))
#imelda=KrInstance(*['Imelda Marcos', 1929, 7, 2, 5, 30, 'Manila', True][:7])
#print(batsc2(NatalAspects(imelda).get_all_aspects()))
#kanye = KrInstance("Kanye", 1977, 6, 8, 8, 45, "Cebu")
#print("hi")
#start = time.time()
#for i in range(0,50*24*60):
#    a=NatalAspects(kanye).get_all_aspects()
#stop = time.time()
#print(start-stop)

#max1 = KrInstance("Max", 2001, 7, 4, 16, 42, "Cebu")
#max2 = KrInstance("Max", 2001, 7, 4, 16, 43, "Cebu")

#a1=max1.uranus.abs_pos-max1.saturn.abs_pos
#a2=max2.uranus.abs_pos-max2.saturn.abs_pos
#print(a2-a1)
while choice != "0":
    init()
    tit("Astrology House Menu")
    opt("Input House Codes + Interpretation", "People","Secondary Progressions", "Aspect Meaning","Relevant Aspect Now","Meaning of 12 Houses", "Tutorial")
    endl()
    if choice == "1":
        tit("Please input House Codes")
        endl()
        house_codes_interp(choice)
    elif choice == "2":
        tit("Select Action")
        opt1 = ["Add"]
        if (len(persons_data) > 0):
            opt1.insert(0, "View People")
            opt1 += ["Edit", "Delete"]
        opt(*opt1)
        endl()
        if (len(persons_data) > 0):
            if choice == "1":
                opt2 = []
                for data in persons_data:
                    opt2.append(data[0])
                tit("Who to view?")
                opt(*opt2)
                endl()
                end()
                tit(persons_data[int(choice) - 1][0])
                end()
                birth_array=birth_info_to_array(*persons_data[int(choice) - 1])
                choice1 = choice
                print(birth_array)
                tit("What to view?")
                opt("House Interpretation","Aspect Interpretation")
                endl()
                if choice in "1":
                    birth_array_to_house_code(birth_array)
                elif choice in "2":
                    secondary_code_to_meaning(birth_array_to_secondary_code(birth_array),birth_array)
            elif choice == "2":
                tit("Add Person Name:")
                endl()
                name = choice
                tit("Add Person Birthday Information")
                bod("Allowed Formats:")
                bod("Month Day, Year (24h hh:mm time format) Place")
                bod("September 19, 2000 2:32 Cebu")
                bod("Month Day, Year Place")
                bod("September 19, 2000 Cebu")
                bod_format("All other inputs will result in calculation error.")
                bod("Not all places are in database.")
                endl()
                code = choice
                persons_data.append([name, code])
                data_save()
            elif choice == "3":
                opt2 = []
                for data in persons_data:
                    opt2.append(data[0])
                tit("Who to edit?")
                opt(*opt2)
                endl()
                editname = int(choice)
                tit("What to edit?")
                opt("Name", "Birthday Information")
                endl()
                opt3 = int(choice)
                tit("Text to edit")
                print(persons_data[editname - 1][opt3 - 1])
                tit("What to replace?")
                endl()
                persons_data[editname - 1][opt3 - 1] = choice
                data_save()
            elif choice == "4":
                opt2 = []
                for data in persons_data:
                    opt2.append(data[0])
                tit("Who to delete?")
                opt(*opt2)
                endl()
                print(choice)
                del persons_data[int(choice) - 1]
                data_save()


        elif choice == "1":
            tit("Add Person Name:")
            endl()
            name = choice
            tit("Add Person Birthday Information")
            bod("Allowed Formats:")
            bod("Month Day, Year (24h hh:mm time format) Place")
            bod("September 19, 2000 2:32 Cebu")
            bod("Month Day, Year Place")
            bod("September 19, 2000 Cebu")
            bod_format("All other inputs will result in calculation error.")
            bod("Not all places are in database.")
            endl()
            code = choice
            persons_data.append([name, code])
            data_save()

    elif choice == "3":
        tit("Enter Secondary Direction Code")
        endl()
        #secondary_directions_meaning
        secondary_code_to_meaning(input_to_filtered_aspects(choice),"AstroSeekCode")

    elif choice == "4":
        tit("Input Aspect in Question")
        endl()
        asp=choice.split(" ")
        asp[1]=ata(asp[1])
        aspect_to_secondary_direction_meaning(asp, "AspectOnly")

    elif choice == "5":

        tit("Input angles to find:")
        bod("e.g., 000, 030, 045, 060, 072")
        bod("      090, 120, 135, 144, 180.")
        bod("Input nothing to search all.")
        endl()
        choice1_1=choice

        tit("Input planets to find:")
        bod("e.g., Pluto, Neptune, Uranus, Saturn")
        bod("      Jupiter, Mars, Sun, Venus")
        bod("      Mercury, Moon")
        bod("Input nothing to search all.")
        endl()
        choice1_4=choice

        tit("Input how many aspects to see:")
        bod("Input nothing to see 1.")
        endl()
        choice1_2=choice

        tit("Input when to start seeing:")
        bod("Format: yyyy-mm-dd hh:mm:ss")
        bod("Input nothing to start in time now.")
        endl()
        choice1_3=choice

        if choice1_3=="":
            see_time=now=datetime.now()
            year=see_time.year
        else:
            year=int(choice1_3.split("-")[0])
            see_time = input1_to_datetime(choice1_3)
        tit(" ( Relevant Aspect Now ) ")
        if not (os.path.exists("aspects/{}.txt".format(year))):
            bod("Please create file for year {0} as {0}.txt in /aspects/".format(year))
        else:
            read_aspects(year,choice1_1,choice1_4)
            aspects=find_next_aspects(see_time,choice1_2,choice1_3)
            aspect_now = KrInstance(*datetime_to_date_array("Barly", see_time, "Cebu"))
            planets_data = [aspect_now.pluto,aspect_now.neptune,aspect_now.uranus,aspect_now.saturn,aspect_now.jupiter,aspect_now.mars,aspect_now.sun,aspect_now.venus,aspect_now.mercury,aspect_now.moon]
            for aspect in aspects:
                aspect[1]=ata(aspect[1])
                aspect_datetime=aspect_to_datetime(aspect)
                tit(" [{}] ".format(aspect_datetime.strftime("%B %d, %Y")))
                tit(" [{} | {}] ".format(aspect_datetime.strftime("%I:%M:%S %p"),aspect[4]))
                tit(" {}-{} Angle: [{}] ".format(*aspect_to_angle(aspect,planets_data)))#["Moon","Mars",num_to_deg(180.52)]))
                aspect_to_secondary_direction_meaning(aspect[:3], "AspectOnly")
                end()
    elif choice == "7":
        for house in house_meanings:
            tit("")
            print(house)
        tit("")

    # moo10 sat10 jup11 mar1leo sun2 mer3 ven3 ura7
