SELECT
	Count(1) totalRows
FROM [DWAPICentral].[dbo].[PatientVisitExtract] PV
INNER JOIN [DWAPICentral].[dbo].[PatientExtract](NoLock) P ON PV.[PatientId]= P.ID AND PV.Voided = 0
INNER JOIN [DWAPICentral].[dbo].[Facility] F ON [FacilityId]  = F.Id  AND F.Voided=0
WHERE visitType = 'scheduled' AND nextAppointmentDate IS NULL AND code = :mfl_code;